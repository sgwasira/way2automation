from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ListTxPage:
    backButton_xpath = ""
    resetButton_xpath = ""

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
