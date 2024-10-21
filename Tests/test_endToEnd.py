import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.accountPage import AccountPage
from Pages.customerPage import CustomerPage
from Pages.loginPage import LoginPage
from Pages.listTxPage import ListTxPage

from Utils.readProperties_UrlDetails import ReadLoginConfig


class Test_01_endToEnd:
    way2automationURL = ReadLoginConfig().getway2automationURL()
    clientNameTest01 = ReadLoginConfig().getClientNameTest01()
    clientNameTest02 = ReadLoginConfig().getClientNameTest02()

    depositAmount = 1500
    withdrawalAmount = 314593

    @pytest.mark.endToEnd
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01Test(self, setup):
        self.driver = setup
        self.driver.get(self.way2automationURL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="CustomerPage_Test01",
                      attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.customer = CustomerPage(self.driver)
        self.customer.selectUser(self.clientNameTest01)
        self.customer.clickLoginBtn()
        allure.attach(self.driver.get_screenshot_as_png(), name="AccountPage_Test01",
                      attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.account = AccountPage(self.driver)
        self.account.clickDepositMenuButton()
        time.sleep(2)
        self.account.enterTransAmount(self.depositAmount)
        time.sleep(2)
        self.account.clickSubmitDepositButton()
        time.sleep(2)
        self.account.getDepositSuccessfulText()
        time.sleep(2)
        self.account.clickLogoutButton()

    @pytest.mark.Test2
    @pytest.mark.endToEnd
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02Test(self, setup):
        self.driver = setup
        self.driver.get(self.way2automationURL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="CustomerPage_Test02",
                      attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.customer = CustomerPage(self.driver)
        self.customer.selectUser(self.clientNameTest02)
        self.customer.clickLoginBtn()
        allure.attach(self.driver.get_screenshot_as_png(), name="AccountPage_Test02",
                      attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.account = AccountPage(self.driver)
        self.account.clickDepositMenuButton()

        numberOfAccounts = self.account.getNumberOfAccounts()
        self.account.depositIntoAllAccounts(1500, numberOfAccounts)

        time.sleep(2)
        self.account.clickLogoutButton()

    @pytest.mark.Test3
    @pytest.mark.endToEnd
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03Test(self, setup):
        self.driver = setup
        self.driver.get(self.way2automationURL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)
        self.login.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="CustomerPage_Test03",
                      attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.customer = CustomerPage(self.driver)
        self.customer.selectUser(self.clientNameTest02)
        self.customer.clickLoginBtn()
        allure.attach(self.driver.get_screenshot_as_png(), name="AccountPage_Test03",
                      attachment_type=AttachmentType.PNG)

        time.sleep(2)

        self.account = AccountPage(self.driver)
        startingBalance = self.account.getStartingBalance()
        self.account.clickDepositMenuButton()
        time.sleep(2)
        self.account.enterTransAmount(self.withdrawalAmount)
        time.sleep(2)
        self.account.clickSubmitDepositButton()
        time.sleep(2)

        self.account.clickTransactionButton()
        time.sleep(2)
        self.listTx = ListTxPage(self.driver)
        self.listTx.verifyCreditTransaction()
        allure.attach(self.driver.get_screenshot_as_png(), name="CreditTransaction_Test03",
                      attachment_type=AttachmentType.PNG)
        self.listTx.clickBackButton()

        self.account = AccountPage(self.driver)
        self.account.clickWithdrawalButton()
        time.sleep(2)
        self.account.enterTransAmount(self.withdrawalAmount)
        time.sleep(2)
        self.account.clickSubmitWithdrawButton()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="DebitTransaction_Test03",
                      attachment_type=AttachmentType.PNG)
        self.account.clickTransactionButton()
        time.sleep(2)

        self.listTx = ListTxPage(self.driver)
        self.listTx.verifyDebitTransaction()
        self.listTx.clickBackButton()

        self.account = AccountPage(self.driver)
        self.account.verifyBalanceAfterWithdrawal(startingBalance)
        time.sleep(2)
        self.account.clickLogoutButton()


