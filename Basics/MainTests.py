import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()  # Ensure that your chromedriver is correctly set up
driver.maximize_window()

# Open the website
driver.get("http://www.way2automation.com/angularjs-protractor/banking/#/login")

# Allow the page to load
time.sleep(5)

# WebDriverWait object
wait = WebDriverWait(driver, 10)

# Page web elements by page
# Home page
customerLoginBtn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary btn-lg'][contains(.,'Customer Login')]")))
bankManagerLoginBtn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary btn-lg'][contains(.,'Bank Manager Login')]")))


customerLoginBtn.click()  # Click the Customer Login button

time.sleep(5)