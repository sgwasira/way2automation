from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:
    noAccountSelector_xpath = "//select[contains(@ng-hide,'noAccount')]"
    depositAmount_xpath = "//input[contains(@type,'number')]"
    depositButton_xpath = "//button[@ng-class='btnClass2'][contains(.,'Deposit')]"
    submitDepositButton_xpath = "//button[@type='submit'][contains(.,'Deposit')]"

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

