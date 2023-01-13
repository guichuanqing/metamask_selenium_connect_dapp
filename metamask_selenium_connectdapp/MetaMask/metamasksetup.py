import time

import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class metamask:
    def metamaskSetup(driver,recoveryPhrase, password):
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/button').click() #点击 开始使用
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click() #点击 我同意
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click() #点击 导入钱包
        time.sleep(3)
        i = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[1]/div/input')
        i.click()
        time.sleep(2)
        print(pyperclip.copy(recoveryPhrase))
        print(pyperclip.paste())
        i.send_keys(Keys.CONTROL,"V")
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
        driver.find_element(By.XPATH,'//*[@id="confirm-password"]').send_keys(password)
        driver.find_element(By.XPATH,'//*[@id="create-new-vault__terms-checkbox"]').click()
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button').click()
        time.sleep(5)
        driver.find_element(By.XPATH,'//*[@id="app-content"]/div/div[2]/div/div/button').click()
        print("Wallet has been imported successfully")


    def connectDapp(driver):
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
