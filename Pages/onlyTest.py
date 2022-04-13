from MainPage import MainPage
from EspressoCoffeePage import EspressoCoffeePage




for i in range(1):
    a = MainPage()
    a.openPage()
    b = EspressoCoffeePage(a.getDriver())
    b.addToCart()
    b.teardown_method()
    print(i)



