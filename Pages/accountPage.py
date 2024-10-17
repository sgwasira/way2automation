from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:
    noAccountSelector_xpath = "//select[contains(@ng-hide,'noAccount')]"
    depositAmount_xpath = "//input[contains(@type,'number')]"
    depositButton_xpath = "//button[@ng-class='btnClass2'][contains(.,'Deposit')]"
    submitDepositButton_xpath = "//button[@type='submit'][contains(.,'Deposit')]"
    transactionButton_xpath = "//button[@ng-class='btnClass1'][contains(.,'Transactions')]"
    withdrawalButton_xpath = "//button[@ng-class='btnClass3'][contains(.,'Withdrawl')]"
    startingBalance_xpath = "//strong[@class='ng-binding'][contains(.,'31515')]"

    def __init__(self, driver):
        self.driver = driver

    def clickDepositMenuButton(self):
        wait = WebDriverWait(self.driver, 10)
        depositButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.depositButton_xpath)))
        depositButton.click()

    def clickSubmitDepositButton(self):
        wait = WebDriverWait(self.driver, 10)
        submitDepositButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.submitDepositButton_xpath)))
        submitDepositButton.click()

    def enterDepositAmount(self, amount):
        wait = WebDriverWait(self.driver, 10)
        depositAmount = wait.until(EC.element_to_be_clickable((By.XPATH, self.depositAmount_xpath)))
        depositAmount.send_keys(amount)

    def selectAccount(self, accountNumber):
        wait = WebDriverWait(self.driver, 10)
        noAccountSelector = wait.until(EC.element_to_be_clickable((By.XPATH, self.noAccountSelector_xpath)))

        # initialise Select class
        noAccount = Select(noAccountSelector)

        # getting the total number of options
        option = noAccount.options

        total_options = len(option)

        # Selecting the first options
        noAccount.select_by_index(accountNumber)

    def clickWithdrawalButton(self):
        wait = WebDriverWait(self.driver, 10)
        withdrawalButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.withdrawalButton_xpath)))
        withdrawalButton.click()

    def clickTransactionButton(self):
        wait = WebDriverWait(self.driver, 10)
        withdrawalButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.withdrawalButton_xpath)))
        withdrawalButton.click()

        

