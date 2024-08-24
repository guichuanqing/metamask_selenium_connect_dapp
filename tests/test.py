# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/8/24 14:34
# @File : test.py
# Description : 文件说明
"""
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_chromedriver_version():
    # 启动一个 WebDriver 实例
    driver_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chromedriver.exe')
    print(driver_path)
    service = Service(executable_path=driver_path)
    chrome_options = Options()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 获取 WebDriver 版本
    version = driver.capabilities['chrome']['chromedriverVersion']
    print(version)
    # 关闭 WebDriver 实例
    driver.quit()

    return version
