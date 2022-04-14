from BasePage import *


class MainPage(BasePage):
    # URLS
    page = "https://www.coffeein.sk/"

    # XPath locators
    cookiesConsentButton = "//button[@class='cc-nb-reject']"
    coffeeForEspressoA = "//ul[@class='left_main_menu']//a[contains(text(),'Káva na espresso')]"

    def __init__(self):
        super().__init__()

    def open_page(self):
        """Open coffeein.sk webpage, reject cookies and click on coffee for espresso section"""
        self.open_web(self.page)
        if self.is_element_displayed(self.cookiesConsentButton):
            print("Cookies consent present.")
            self.my_click(self.cookiesConsentButton)
        self.my_click(self.coffeeForEspressoA)
