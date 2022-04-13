from BasePage import *


class MainPage(BasePage):
    # URLS
    page = "https://www.coffeein.sk/"

    # XPath locators
    cookiesConsentButton = "//button[@class='cc-nb-reject']"
    coffeeForEspressoA = "//ul[@class='left_main_menu']//a[contains(text(),'Káva na espresso')]"

    def __init__(self):
        super().__init__()

    def openPage(self):
        self.openWeb(self.page)
        if self.isElementDisplayed(self.cookiesConsentButton):
            self.myClick(self.cookiesConsentButton)
        self.myClick(self.coffeeForEspressoA)
