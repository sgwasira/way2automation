from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AccountPage:
    noAccountSelector_xpath = "//select[contains(@ng-hide,'noAccount')]"
    transAmount_xpath = "//input[contains(@type,'number')]"
    depositButton_xpath = "//button[@ng-class='btnClass2'][contains(.,'Deposit')]"
    submitDepositButton_xpath = "//button[@type='submit'][contains(.,'Deposit')]"
    transactionButton_xpath = "//button[@ng-class='btnClass1'][contains(.,'Transactions')]"
    withdrawalButton_xpath = "//button[@ng-class='btnClass3'][contains(.,'Withdrawl')]"
    startingBalance_xpath = "(//strong[@class='ng-binding'][contains(.,'0')])[2]"
    logoutButton_xpath = "//button[@ng-show='logout'][contains(.,'Logout')]"
    depositSuccessfulText_xpath = "//span[@class='error ng-binding'][contains(.,'Deposit Successful')]"

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

    def enterTransAmount(self, amount):
        wait = WebDriverWait(self.driver, 10)
        depositAmount = wait.until(EC.element_to_be_clickable((By.XPATH, self.depositAmount_xpath)))
        depositAmount.send_keys(amount)

    def clickWithdrawalButton(self):
        wait = WebDriverWait(self.driver, 10)
        withdrawalButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.withdrawalButton_xpath)))
        withdrawalButton.click()

    def clickTransactionButton(self):
        wait = WebDriverWait(self.driver, 10)
        withdrawalButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.withdrawalButton_xpath)))
        withdrawalButton.click()

    def clickLogoutButton(self):
        wait = WebDriverWait(self.driver, 10)
        logoutButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.logoutButton_xpath)))
        logoutButton.click()

    def getDepositSuccessfulText(self):
        wait = WebDriverWait(self.driver, 20)
        depositSuccessfulText = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.depositSuccessfulText_xpath)))
        depositSuccessfulText.is_displayed()

    def getNumberOfAccounts(self):
        wait = WebDriverWait(self.driver, 20)

        noAccountSelector = wait.until(EC.element_to_be_clickable((By.XPATH, self.noAccountSelector_xpath)))

        # initialise Select class
        noAccount = Select(noAccountSelector)

        # getting the total number of options
        option = noAccount.options

        total_options = len(option)
        return total_options

    def depositIntoAllAccounts(self, amount, numberOfAmount):
        wait = WebDriverWait(self.driver, 10)
        noAccountSelector = wait.until(EC.element_to_be_clickable((By.XPATH, self.noAccountSelector_xpath)))
        submitDepositButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.submitDepositButton_xpath)))

        # initialise Select class
        noAccount = Select(noAccountSelector)

        i = 0
        while i < numberOfAmount:
            # Selecting the account options
            noAccount.select_by_index(i)
            depositAmount = wait.until(EC.element_to_be_clickable((By.XPATH, self.depositAmount_xpath)))
            depositAmount.send_keys(amount)
            time.sleep(2)
            submitDepositButton.click()

            time.sleep(2)
            depositSuccessfulText_element = wait.until(EC.visibility_of_element_located(
                (By.XPATH, self.depositSuccessfulText_xpath))).text

            assert depositSuccessfulText_element == "Deposit Successful", "The amount was not deposited into the account"
            i += 1

    def getStartingBalance(self):
        wait = WebDriverWait(self.driver, 10)
        startingBalance = wait.until(EC.element_to_be_clickable((By.XPATH, self.startingBalance_xpath))).getText()

        return startingBalance

    def verifyBalanceAfterWithdrawal(self, gStartingBalance):
        wait = WebDriverWait(self.driver, 10)
        balanceAfterWithdrawal = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.startingBalance_xpath))).getText()
        assert balanceAfterWithdrawal == gStartingBalance, "The amount was not deposited into the account"
