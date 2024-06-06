from Pages.loginPage import Login
def test_LoginDifferentCredential(browser):
    p1=Login(browser)
    p1.checkWithFiveValidCredential()

# ShoppersStackProject1/test/test_loginFiveDifferenctCredential.py
