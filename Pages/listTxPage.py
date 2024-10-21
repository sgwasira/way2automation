from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ListTxPage:
    backButton_xpath = "//button[@class='btn'][contains(.,'Back')]"
    resetButton_xpath = "//button[@ng-show='showDate'][contains(.,'Reset')]"
    creditCheck_element_xpath = "(//td[contains(@class,'ng-binding')])[3]"
    debitCheck_element_xpath = "(//td[contains(@class,'ng-binding')])[6]"

    def __init__(self, driver):
        self.driver = driver

    def clickBackButton(self):
        wait = WebDriverWait(self.driver, 10)
        backButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.backButton_xpath)))
        backButton.click()

    def clickResetButton(self):
        wait = WebDriverWait(self.driver, 10)
        resetButton = wait.until(EC.element_to_be_clickable((By.XPATH, self.resetButton_xpath)))
        resetButton.click()

    def verifyCreditTransaction(self):
        wait = WebDriverWait(self.driver, 10)
        creditCheck_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.creditCheck_element_xpath)))
        creditCheck_element.is_displayed()

    def verifyDebitTransaction(self):
        wait = WebDriverWait(self.driver, 10)
        debitCheck_element = wait.until(EC.element_to_be_clickable((By.XPATH, self.debitCheck_element_xpath)))
        debitCheck_element.is_displayed()


