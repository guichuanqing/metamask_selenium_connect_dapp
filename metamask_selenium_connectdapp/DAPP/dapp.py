from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def dappclick(driver):
    driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/nav/div/div[3]/div/span/div/button[1]').click()
    driver.find_element(By.XPATH,'/html/body/reach-portal/div[3]/div/div/div/div/div/div[3]/div/div[1]/button[1]').click()