from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def dapp_click(driver):
    # 判断dapp是否已经登录
    try:
        elmt_acct = driver.find_element(By.XPATH,'//*[@id="AppHeader"]/div[2]/nav/div/div[3]/div[2]/button/div[2]/span')
        if elmt_acct.is_displayed():
            print("dapp已经登录")
            return False
    except NoSuchElementException:
        driver.find_element(By.XPATH, '//*[@id="AppHeader"]/div[2]/nav/div/div[3]/div[3]/div/button').click()
        driver.find_element(By.XPATH,
                            '//*[@id="wallet-dropdown-scroll-wrapper"]/div/div/div[5]/div[1]/div/div[1]/button').click()
        print("dapp登录成功")
        return True