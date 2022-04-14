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
    finishOrder = "//div[@id='finish_order']"

    # Variables
    orderByPriceValue = 'pr_price'  # Value for ordering by price
    orderByDescValue = 'DESC'  # Value for descending order

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        """
        Change filter to order by price,
        then change ordering to be descending,
        add first item to cart,
        wait for finish order button to appear,
        add second item to cart,
        assert if there are 2 items in cart.
         """
        self.select_from_dropdown(self.orderByDropdown, self.orderByPriceValue)
        self.select_from_dropdown(self.orderByAscDescDropdown, self.orderByDescValue)
        self.my_click(self.firstMostExpensive)
        self.wait_and_find(self.finishOrder)

        # This is ugly, but i didn't figure out how to bypass the animation
        time.sleep(0.5)

        self.my_click(self.secondMostExpensive)
        self.wait_and_find(self.cartCounterTwo)
        assert self.get_text(self.cartCounter) == "2", "there should be 2 things in the cart counter"

    def click_unclickable(self):
        """Click element which is not present"""
        self.my_click(self.finishOrder)
