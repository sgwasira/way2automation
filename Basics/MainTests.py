import time

import click
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # This starts the session
driver.maximize_window()
driver.get("http://www.way2automation.com/angularjs-protractor/banking/#/login")

time.sleep(5)

driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-lg'][contains(.,'Customer Login')]").click()
