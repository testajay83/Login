from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
driver.maximize_window()
driver.get("https://dev-client.mycarauction.com/login")
driver.find_element_by_name("email").send_keys("sam@strategiceis.com")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_class_name("btn.btn-danger.d-block.w-100.round--corner.mg-b-20").click()
#GetMyEstimate(Screen)
driver.get("https://dev-client.mycarauction.com/landing-page")
#driver.find_element_by_id("search-by-plate").send_keys("3D73Y3CL6BG585460")
#select = driver.find_element_by_id("search-by-state")
#drp = Select(select)
#drp.select_by_value("AK")
#driver.find_element_by_id("search-by-vin").send_keys("3D73Y3CL6BG585460")
select = driver.find_element_by_id("search-filter-year")
drp = Select(select)
drp.select_by_visible_text("2021")
wait = WebDriverWait(driver, 10).until(expected_conditions.
                                       element_to_be_clickable((By.NAME, "manufacturer"))
                                       )
drp = Select(wait)
drp.select_by_visible_text("RAM")
wait = WebDriverWait(driver, 10).until(expected_conditions.
                                       element_to_be_clickable((By.NAME, "models"))
                                       )
drp = Select(wait)
drp.select_by_visible_text("3500 4WD 6C TDSL")
wait = WebDriverWait(driver, 10).until(expected_conditions.
                                       element_to_be_clickable((By.NAME, "Style"))
                                       )
drp = Select(wait)
drp.select_by_visible_text("MEGA CAB 6.7L BIG HORN")
wait = WebDriverWait(driver, 10).until(expected_conditions.
                                       element_to_be_clickable((By.ID, "search-filter-color"))
                                       )
drp = Select(wait)
drp.select_by_visible_text("Yellow")

driver.find_element(By.ID, "search-estimate-btn").click()

























