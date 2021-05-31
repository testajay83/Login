from selenium import webdriver
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
driver.maximize_window()
driver.get("https://dev-client.mycarauction.com/login")
driver.find_element_by_name("email").send_keys("sam@strategiceis.com")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_class_name("btn.btn-danger.d-block.w-100.round--corner.mg-b-20").click()

# GetMyEstimate(Screen)
driver.get("https://dev-client.mycarauction.com/landing-page")
driver.find_element(By.ID, "search-by-plate").send_keys("3D73Y3CL6BG585460")
select = driver.find_element(By.ID, "search-by-state")
drp = Select(select)
drp.select_by_value("AK")
wait = WebDriverWait(driver, 20).until(expected_conditions.
                                       element_to_be_clickable((By.ID, "search-filter-color"))
                                       )
drp = Select(wait)
drp.select_by_visible_text("Yellow")

driver.find_element(By.ID, "search-estimate-btn").click()

wait = WebDriverWait(driver, 60).until(expected_conditions.
                                       presence_of_element_located((By.CLASS_NAME, "basic__car"))
                                       )

driver.find_element(By.ID, "enter-zip-code").send_keys('92620')

driver.find_element(By.ID, "mileage-target").send_keys('10000')

# For Edit
# driver.find_element(By.CLASS_NAME,"edits__links.font-medium").click()

#Salvage
#driver.find_element(By.ID,"enter-title-salvage").click()
#driver.find_element(By.CLASS_NAME,"swal-button.swal-button--OK").click()

#Clean:
#wait = WebDriverWait(driver, 60).until(expected_conditions.
#                                       visibility_of_element_located((By.CLASS_NAME, "textbox__info--icon"))
#                                       )
driver.implicitly_wait(20)

target = driver.find_element(By.ID, "enter-title-clean")
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
driver.execute_script('arguments[0].scrollIntoView(true);', target)
target.click()
#driver.find_element(By.ID, "enter-title-clean").click()
# Cases of clean:
# 1.Title in Hand
driver.find_element(By.ID, "title-in-hand").click()

# 2.Loan
#driver.find_element(By.ID,"loan").click()
#driver.find_element(By.ID,"enter-loan-payOff").send_keys("1000")
#driver.find_element(By.ID,"loan-payOff-submit").click()

# 3.Lease
# driver.find_element(By.ID,"lease").click()
# driver.find_element(By.ID,"enter-loan-payOff").send_keys(200)
# driver.find_element(By.ID,"loan-payOff-submit").click()
driver.implicitly_wait(20)

#target = driver.find_element(By.CLASS_NAME, 'basic__car')
#target = driver.find_element(By.ID, "edit-features-link")
#actions = ActionChains(driver)
#actions.move_to_element(target)
#actions.perform()
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#driver.execute_script('arguments[0].scrollIntoView(true);', target)
#target.click()
#driver.implicitly_wait(20)
# Basic(Edit-Clean)

wait = WebDriverWait(driver, 60).until(expected_conditions.
                                       presence_of_element_located((By.CLASS_NAME, "basic__car"))
                                       )
#driver.find_element(By.CSS_SELECTOR, "#headingOne .basic__accordian--headright a").click();

#wait = WebDriverWait(driver, 60).until(expected_conditions.
                                       #presence_of_element_located((By.CLASS_NAME, "basic__car"))
                                       #)

# Car located Textbox(Edit Mode):
#(Edit zipCode)
#driver.find_element(By.ID, "edit-zip-code").clear()
#driver.find_element(By.ID, "edit-zip-code").send_keys('92618')
#Mileage(Edit Mode):
#driver.find_element(By.ID, "edit-mileage-target").send_keys("1001")
# Clean(Edit Mode):
#driver.find_element(By.ID, "edit-title-clean").click()
# Salvage(edit Mode):
# driver.find_element(By.ID,"edit-title-salvage").click()
# driver.find_element(By.CLASS_NAME,"swal-button.swal-button--OK").click()
# (Title in Hand)(Edit Mode):
# driver.find_element(By.ID,"edit-title-in-hand").click()
# Loan(Edit Mode)
#driver.find_element(By.ID,"edit-loan").click()
#driver.find_element(By.ID,"loan-amount").send_keys('3000')
# Lease(Edit Mode)
# driver.find_element(By.ID,"edit-lease").click()
# driver.find_element(By.ID,"loan-amount").send_keys('400')

# NextEditMode
#driver.find_element(By.ID,"edit-comp-next").click()

# EditIn(Vehicle)
#driver.find_element(By.ID,"edit-features-link").click()

# Show More:
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#driver.find_element(By.ID,"show-all-features-btn").click()
#driver.execute_script("window.scroll(0,0);")
target = driver.find_element(By.ID, "show-all-features-btn")
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
driver.execute_script('arguments[0].scrollIntoView(true);', target)
target.click()
#driver.execute_script("window.scroll(0,0);")ipt('arguments[0].scrollIntoView(true);', target)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#top of the page
#driver.implicitly_wait(30)
time.sleep(20)

#driver.find_element(By.CLASS_NAME,"btn.btn-blue.btn__big.min-w280").click()
#time.sleep(4)
#driver.find_element(By.ID, "show-all-features-btn").click()
#driver.find_element(By.NAME, "Pwr locks").is_selected()
#target = driver.find_element(By.NAME, "Pwr locks").click()
#actions = ActionChains(driver)
#actions.move_to_element(target)
#actions.perform()
#driver.execute_script('arguments[0].scrollIntoView(true);', target)
#target.click()
arr = ["Manual shift-on-the-fly transfer case", "Dual rear wheels", "Four wheel drive", "Pwr locks"]
for x in arr:
    ch = driver.find_element(By.NAME, x)
    ch.is_selected = True
#loop on array
#for arr {
#ch = driver.find_element(By.CLASS_NAME, "custom-check-new") / input[contains(text(), x)]
    #ch = driver.find_element(By.CLASS_NAME, "custom-check-new")/input[contains(text(), arr[i])]
#}

#ch = driver.find_element(By.CLASS_NAME, "custom-check-new")/input[contains(text(), "Audio input jack")]
#print(ch)

#target = driver.find_element(By.NAME, "CHROME ACCENTS GROUP")
#actions = ActionChains(driver)
#actions.move_to_element(target)
#actions.perform()
#driver.execute_script('arguments[0].scrollIntoView(true);', target)
#target.click()
#driver.find_element(By.CLASS_NAME,"btn.btn-blue.btn__big min-w280").click()







