import unittest
import os
from selenium import webdriver
from MainPage import MainPage
from EspressoCoffeePage import EspressoCoffeePage


class CoffeeTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(os.getcwd() + '\\chromedriver.exe')
        self.driver.delete_all_cookies()
        self.addCleanup(self.driver.quit)
        self.addCleanup(self.screen_shot)
        self.driver.implicitly_wait(5)

    def screen_shot(self):
        for method, error in self._outcome.errors:
            if error:
                self.driver.get_screenshot_as_file("screenshot" + self.id() + ".png")

    def test_coffee_pass(self):
        main_page = MainPage(self.driver)
        main_page.open_page()
        espresso_coffee_page = EspressoCoffeePage(main_page.get_driver())
        espresso_coffee_page.add_to_cart()

    # def test_coffee_fail(self):
    #     main_page = MainPage(self.driver)
    #     main_page.open_page()
    #     espresso_coffee_page = EspressoCoffeePage(main_page.get_driver())
    #     espresso_coffee_page.click_unclickable()


if __name__ == '__main__':
    unittest.main()
