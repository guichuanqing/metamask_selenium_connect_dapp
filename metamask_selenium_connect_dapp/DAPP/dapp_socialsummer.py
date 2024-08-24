from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time




class SocialSummer():
    def __init__(self):
        self.dapp_url = "https://socialsummer.ai/"

    def dapp_setup(self, driver):
        driver.get(self.dapp_url)
        time.sleep(3)
        try:
            elmt_acct = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div/div/div[1]/a/img')
            if elmt_acct.is_displayed():
                return True
        except NoSuchElementException:
            return False

    def dapp_click(self, driver):
        try:
            if not self.get_login_stat(driver):
                driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div/div/div[3]/div/button').click()
                driver.find_element(By.XPATH,
                                    '//*[@id="w3m"]/div[2]/div/div/div/div[2]/div/div[1]').click()  # 点击Metamask
                print("dapp开始连接Metamask")
                return True
        except NoSuchElementException:
            print('页面加载失败')
            return False

    def get_login_stat(self, driver):
        # 判断dapp是否已经登录
        try:
            elmt_acct = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div/div/div[3]/div/button')
            if elmt_acct.is_displayed():
                if elmt_acct.text != "登录" and elmt_acct.text != "Login":
                    print("dapp已登录")
                    return True
            print("dapp未登录")
            return False
        except NoSuchElementException:
            print('页面加载失败')
            return False
