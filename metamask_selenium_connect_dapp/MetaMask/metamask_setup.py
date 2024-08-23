import time

import pyperclip
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MetaMask:
    def __init__(self):
        # 导入助记词
        self.recoveryPhrase = "cloud shove firm between fog faculty photo early output artwork woman scatter"
        self.password = '12345678'
    def home_setup(self, driver):
        try:
            elmt_title = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/h1')
            if elmt_title.is_displayed():
                driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password) #输入密码
                driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click() #点击登录
                time.sleep(5)
                elmt_addr = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div/div/button/span[1]/span')
                if elmt_addr.is_displayed():
                    print("钱包登录成功")
                    time.sleep(1)
                    driver.close()
                    return True
                else:
                    print("登录失败")
                    return False
        except NoSuchElementException:
            try:
                time.sleep(3)
                elmt_login_title = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div/span[2]')
                if elmt_login_title.is_displayed():
                    print("钱包已登录")
                    time.sleep(1)
                    driver.close()
                    return True
            except NoSuchElementException:
                print("登录初始化失败")
                return False
    def metamask_account_init(self, driver,recoveryPhrase, password):
        driver.find_element(By.XPATH, '//*[@id="onboarding__terms-checkbox"]').click() #点击 我同意
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[3]/button').click() #点击 导入钱包
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button[2]').click()  # 点击 我同意
        time.sleep(3)
        i = driver.find_element(By.XPATH,'//*[@id="import-srp__srp-word-0"]')
        i.click()
        time.sleep(2)
        print(pyperclip.copy(recoveryPhrase))
        print(pyperclip.paste())
        i.send_keys(Keys.CONTROL,"V")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button').click()  # 点击 确认私钥助记词
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(password)
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(password)
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click()
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click() # 点击创建钱包
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()  # 点击 知道了
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()  # 点击 下一步
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button').click()  # 点击 完成
        # 尝试次数
        max_retries = 3
        wait_time = 3  # 等待时间（秒）
        for attempt in range(max_retries):
            try:
                element = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[1]/button/svg')
                if element.is_displayed():
                    break
                else:
                    print(f"等待应用加载，尝试次数 {attempt + 1}/{max_retries} s")
            except NoSuchElementException:
                # 等待一段时间后重试
                time.sleep(wait_time)
        driver.close()
        print("Wallet has been imported successfully")

    def connect_dapp(self, driver):
        try:
            print("等待插件启动")
            time.sleep(5)
            # 查找元素
            NO_passwd_element = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/p')
            passwd_element = driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/p')
            # 检查元素是否显示在页面上
            if NO_passwd_element.is_displayed():
                print("开始连接钱包")
                driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]').click()  # 点击 下一步
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '//*[@id="app-content"]/div/div/div/div[3]/div[2]/footer/button[2]').click()  # 点击 链接
                print("钱包连接成功！")
            elif passwd_element.is_displayed():
                print("未登录，输入密码中")
                driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)
                driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/div/div/button').click()
                time.sleep(2)
                driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        except NoSuchElementException:
            print(f"钱包链接失败")
