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

# account page web elements
noAccountSelector = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@ng-hide,'noAccount')]")))
depositButton_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@ng-class='btnClass2'][contains(.,'Deposit')]")))

# initialise Select class
noAccount = Select(noAccountSelector)

# getting the total number of options
option = noAccount.options

total_options = len(option)

i = 0
while i < total_options:
    # Selecting the account options
    noAccount.select_by_index(i)

    # click on the deposit button
    depositButton_element.click()

    # Account page web element
    depositAmount_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@type,'number')]")))
    submitDepositButton_element = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][contains(.,'Deposit')]")))

    depositAmount_element.send_keys("1500")
    submitDepositButton_element.click()

    # Account page web element
    depositSuccessfulText_element = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='error ng-binding'][contains(.,'Deposit Successful')]"))).text

    assert depositSuccessfulText_element == "Deposit Successful", "The amount was not deposited into the account"

    time.sleep(5)
    i += 1

logoutButton_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@ng-show='logout'][contains(.,'Logout')]")))
logoutButton_element.click()
