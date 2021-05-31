import time
import content as content
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from threading import Timer
import selenium
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/notification_message_rendered')
#driver.find_element(By.XPATH, "//*[@id=content]/div/p/a").click()

for loop in range(10):
    d = driver.find_elements(By.CLASS_NAME, "example")[0].find_element(By.TAG_NAME, "a")
    d.click()
    #time.sleep(5)
    #print('start')
    z = driver.find_element(By.CLASS_NAME, "flash notice")[0].find_element(By.TAG_NAME, "a")
    #z.get_attribute('text')class="flash notice"
    print(z)
    #print('end')
    if z == 'Action successful':
        print("pass")
        break

