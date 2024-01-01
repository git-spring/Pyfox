
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://www.bilibili.com/')
browser.find_element(By.CLASS_NAME,"nav-search-input").send_keys("巫师3狂猎")
sleep(1)
browser.find_element(By.CLASS_NAME,"nav-search-btn").click()

import pytest
# browser.quit()
