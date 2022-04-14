from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome(os.getcwd() + '\\chromedriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def select_from_dropdown(self, xpath_dropdown, value):
        Select(self.driver.find_element(By.XPATH, xpath_dropdown)).select_by_value(value)
        print("Selected from dropdown " + xpath_dropdown + " value " + value)

    def my_click(self, xpath):
        self.wait_for_element_to_be_clickable(xpath, 5)
        self.driver.find_element(By.XPATH, xpath).click()
        print("Clicked on element " + xpath)

    def open_web(self, web_url):
        self.driver.get(web_url)
        self.driver.maximize_window()
        print("Opened webpage " + web_url + " and maximized window")

    def get_driver(self):
        return self.driver

    def wait_and_find(self, xpath):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        print("Found element " + xpath)

    def wait_for_element_to_be_clickable(self, xpath, seconds=10):
        WebDriverWait(self.driver, seconds).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    def get_text(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).text

    def is_element_displayed(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).is_displayed()
