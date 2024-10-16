import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Edge()  # Ensure that your chromedriver is correctly set up
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
userSelect_selector.select_by_visible_text("Ron Weasly")

# Customer page web elements
customerLoginSelectedUserBtn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default'][contains(.,'Login')]")))
customerLoginSelectedUserBtn.click()

time.sleep(3)

# account page web elements
noAccountSelector = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@ng-hide,'noAccount')]")))
depositButton_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@ng-class='btnClass2'][contains(.,'Deposit')]")))

# initialise Select class
noAccount = Select(noAccountSelector)

# getting the total number of options
option = noAccount.options

total_options = len(option)

# Selecting the first options
noAccount.select_by_index(0)

# getting the current balance
currentAccountBalance = driver.find_element(By.XPATH, "(//strong[@class='ng-binding'][contains(.,'0')])[2]").text

# click on the deposit button
depositButton_element.click()

# Account page web element
# depositing into acc
depositAmount_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@type,'number')]")))
submitDepositButton_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][contains(.,'Deposit')]")))

depositAmount_element.send_keys("31459")
submitDepositButton_element.click()
time.sleep(1)
# end of depositing into acc


# Account page web element
# Asserting if the transaction was successful
depositSuccessfulText_element = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//span[@class='error ng-binding'][contains(.,'Deposit Successful')]"))).text

assert depositSuccessfulText_element == "Deposit Successful"
# End of assert

# Transaction page web
# Verify that the transaction appears on the ListTx page
transactionButton_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@ng-class='btnClass1'][contains(.,'Transactions')]")))

transactionButton_element.click()
time.sleep(3)

# transaction page web elements
depositedAmountText_element = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//td[@class='ng-binding'][contains(.,'31459')]"))).text
backButton_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn'][contains(.,'Back')]")))

assert depositedAmountText_element == "31459", "The deposit you made was not successful"
backButton_element.click()
# End of Validate of transaction

time.sleep(3)

# transaction page web
# Withdrawal action

withdrawalAmountButton_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@ng-class='btnClass3'][contains(.,'Withdrawl')]")))
withdrawalAmountButton_element.click()

time.sleep(3)

withdrawalAmount = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@type,'number')]")))
submitWithdrawalButton = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][contains(.,'Withdraw')]")))

withdrawalAmount.send_keys("31459")
submitWithdrawalButton.click()
time.sleep(2)

# End of withdraw
transactionButton_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@ng-class='btnClass1'][contains(.,'Transactions')]")))
transactionButton_element.click()
time.sleep(2)

# Verify that the withdrawal transaction was successful

withdrawalTransactionType_element = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//td[@class='ng-binding'][contains(.,'Debit')]"))).text
assert withdrawalTransactionType_element == 'Debit', 'The withdrawal you made was not successful'

backButton_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn'][contains(.,'Back')]")))
backButton_element.click()

# end of verification
time.sleep(2)

# Verify the that the current balance is the same with the original
currentAccountBalanceAfterWithdrawal = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//strong[@class='ng-binding'][contains(.,'0')])[2]"))).text

assert currentAccountBalance == currentAccountBalanceAfterWithdrawal, 'The balances are not the same '
# End of verification

time.sleep(2)

# logging out of the system
logoutButton_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@ng-show='logout'][contains(.,'Logout')]")))
logoutButton_element.click()
