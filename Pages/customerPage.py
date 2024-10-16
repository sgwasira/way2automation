from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerPage:
    userSelect_xpath = "//select[contains(@id,'userSelect')]"
    customerLoginSelectedUserBtn_xpath = "//button[@class='btn btn-default'][contains(.,'Login')]"

    def __init__(self, driver):
        self.driver = driver

    def selectUser(self, accountUsername):
        wait = WebDriverWait(self.driver, 10)
        userSelect = wait.until(EC.visibility_of_element_located((By.XPATH, self.userSelect_xpath)))

        # customer page actions
        userSelect_selector = Select(userSelect)
        userSelect_selector.select_by_visible_text(accountUsername)

    def clickLoginBtn(self):
        wait = WebDriverWait(self.driver, 10)
        customerLoginBtn = wait.until(EC.element_to_be_clickable((By.XPATH, self.customerLoginSelectedUserBtn_xpath)))
        customerLoginBtn.click()



