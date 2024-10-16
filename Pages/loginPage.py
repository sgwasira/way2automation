from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    button_login_xpath = "//button[@class='btn btn-primary btn-lg'][contains(.,'Customer Login')]"
    bankManager_login_xpath = "//button[@class='btn btn-primary btn-lg'][contains(.,'Bank Manager Login')]"

    def __init__(self, driver):
        self.driver = driver

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        loginElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        loginElement.click()

    def clickBankManagerButton(self):
        wait = WebDriverWait(self.driver, 10)
        BankManagerElement = wait.until(EC.visibility_of_element_located((By.XPATH, self.bankManager_login_xpath)))
        BankManagerElement.click()
