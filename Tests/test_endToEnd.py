import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.accountPage import AccountPage
from Pages.customerPage import CustomerPage
from Pages.loginPage import LoginPage

from Utils.readProperties_UrlDetails import ReadLoginConfig


class Test_01_endToEnd:
    way2automationURL = ReadLoginConfig().getway2automationURL()
    clientNameTest01 = ReadLoginConfig().getClientNameTest01()
    depositAmount = 1500

    @pytest.mark.endToEnd
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01Test(self, setup):
        self.driver = setup
        self.driver.get(self.way2automationURL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Customer Page", attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.customer = CustomerPage(self.driver)
        self.customer.selectUser(self.clientNameTest01)
        self.customer.clickLoginBtn()
        allure.attach(self.driver.get_screenshot_as_png(), name="Account Page", attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.account = AccountPage(self.driver)
        self.account.clickDepositMenuButton()
        time.sleep(2)
        self.account.enterDepositAmount(self.depositAmount)
        time.sleep(2)
        self.account.clickSubmitDepositButton()
        time.sleep(2)
        self.account.getDepositSuccessfulText()
        time.sleep(2)
        self.account.clickLogoutButton()
