from Pages import MainPage
from Pages.EspressoCoffeePage import EspressoCoffeePage


for i in range(20):
    a = MainPage.MainPage()
    a.openPage()
    b = EspressoCoffeePage(a.getDriver())
    b.addToCart()
    b.teardown_method()
    print(i)



