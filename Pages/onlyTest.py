from MainPage import MainPage
from EspressoCoffeePage import EspressoCoffeePage
import os


def first_buy_coffee_test():
    a = MainPage()
    a.open_page()
    b = EspressoCoffeePage(a.get_driver())
    b.add_to_cart()
    b.teardown_method()
    print(".|.|.|- Test passed -|.|.|.")


if __name__ == "__main__":
    first_buy_coffee_test()
