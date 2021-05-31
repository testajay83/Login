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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
driver.maximize_window()
#a).Assert broken images
driver.get("http://the-internet.herokuapp.com/broken_images")
x = driver.find_element(By.CLASS_NAME,"example").find_elements_by_tag_name("img")
for img in x:
    imagePath = img.get_attribute("src")
    resp = requests.get(imagePath)
    if resp.status_code == 404:
        print(imagePath + " Not found" )
    else:
        print(imagePath + " Found")
driver.close()
    #print(resp.status_code)

 #b.forgot password success message:
driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/forgot_password")
Url = "http://the-internet.herokuapp.com/forgot_password"
driver.find_element(By.ID,"email").send_keys("ajay@gmail.com")
a = requests.post(Url,{"email":'ajay@gmail.com'})
driver.find_element(By.ID,"form_submit").click()
if a.status_code != 200:
    print("User not found")
else:
    print("User found")
driver.close()

#c.Assert form validation functionality Post entering a dummy username and password:
driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
driver.find_element(By.ID,"username").send_keys("username")
driver.find_element(By.ID,"password").send_keys("password")
driver.find_element(By.CLASS_NAME,"fa.fa-2x.fa-sign-in").click()
time.sleep(2)
try:
 c = driver.find_element(By.CLASS_NAME,"error")
 print("Fail")
except NoSuchElementException:
        print("Invalid")
driver.close()

#d:Write a test to enter alphabets on this and mark it as a failure if we cannot enter on page:
driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")
driver.implicitly_wait(20)
d1 = driver.find_elements(By.CLASS_NAME, "example")[0].find_element(By.TAG_NAME, "input")
d1.send_keys('a')
m = d1.get_attribute("value")
print(m)
if m != 'a':
  print("fail")
driver.close()
  
#E:Write a test to sort the table by the amount due on page http://the-internet.herokuapp.com/tables
#driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
#driver.maximize_window()
#driver.get("http://the-internet.herokuapp.com/tables")



#F: Right a looped script to assert a 'successful notification" after repeated unsuccessful notification on page http://the-internet.herokuapp.com/notification_message_rendered
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































#arr = ["asdf.jpg", "hjkl.jpg", "img/avatar-blank.jpg"]
#for x in arr:
    #ch = driver.find_element(By.TAG_NAME, "x")
