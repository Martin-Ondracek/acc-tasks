from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def selectFromDropdown(self, xpathDropdown, value):
        Select(self.driver.find_element_by_xpath(xpathDropdown)).select_by_value(value)

    def myClick(self, xpath):
        self.waitForElementToBeClickable(xpath, 5)
        self.driver.find_element_by_xpath(xpath).click()

    def openWeb(self, webUrl):
        self.driver.get(webUrl)
        self.driver.maximize_window()

    def getDriver(self):
        return self.driver

    def waitAndFind(self, xpath):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def waitForElementToBeClickable(self, xpath, seconds=10):
        WebDriverWait(self.driver, seconds).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    def getText(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text



