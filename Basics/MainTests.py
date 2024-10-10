import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()  # Ensure that your chromedriver is correctly set up
driver.maximize_window()

# Open the website
driver.get("http://www.way2automation.com/angularjs-protractor/banking/#/login")

# Allow the page to load
time.sleep(2)

# WebDriverWait object
wait = WebDriverWait(driver, 5)

# login page web elements
customerLoginBtn = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//button[@class='btn btn-primary btn-lg'][contains(.,'Customer Login')]")))
bankManagerLoginBtn = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//button[@class='btn btn-primary btn-lg'][contains(.,'Bank Manager Login')]")))

# login page actions
customerLoginBtn.click()  # Click the Customer Login button

# Customer page web elements
userSelect = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'userSelect')]")))

# customer page actions
userSelect_selector = Select(userSelect)
userSelect_selector.select_by_visible_text("Hermoine Granger")

# Customer page web elements
customerLoginSelectedUserBtn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default'][contains(.,'Login')]")))
customerLoginSelectedUserBtn.click()


time.sleep(5)
