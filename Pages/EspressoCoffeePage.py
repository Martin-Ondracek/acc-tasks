from BasePage import BasePage
import time


class EspressoCoffeePage(BasePage):

    # XPath locators
    orderByDropdown = "//select[@name='filter_radenie_co']"
    orderByAscDescDropdown = "//select[@name='filter_radenie_ako']"
    firstMostExpensive = "(//ul[@class='product_list']//li[contains(@class,'product')])[1]//div[@class='prod_cta']"
    secondMostExpensive = "(//ul[@class='product_list']//li[contains(@class,'product')])[2]//div[@class='prod_cta']"
    cartCounterTwo = "//span[@id='sc_count' and text()='2']"
    cartCounter = "//span[@id='sc_count']"
    finisOrder = "//div[@id='finish_order']"

    # Variables
    orderByPriceValue = 'pr_price'
    orderByDescValue = 'DESC'

    def __init__(self, driver):
        self.driver = driver

    def addToCart(self):
        self.selectFromDropdown(self.orderByDropdown, self.orderByPriceValue)
        self.selectFromDropdown(self.orderByAscDescDropdown, self.orderByDescValue)
        self.myClick(self.firstMostExpensive)
        self.waitAndFind(self.finisOrder)

        # This is ugly, but i didn't figure out how to bypass the animation
        time.sleep(0.5)

        self.myClick(self.secondMostExpensive)
        self.waitAndFind(self.cartCounterTwo)
        assert self.getText(self.cartCounter) == "2", "there should be 2 things in the cart counter"
