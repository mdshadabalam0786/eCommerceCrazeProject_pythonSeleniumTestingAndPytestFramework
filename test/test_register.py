from Pages.registerPage import Register

def test_shopperRegister(browser):
    r1=Register(browser)
    r1.shopperRegister()
