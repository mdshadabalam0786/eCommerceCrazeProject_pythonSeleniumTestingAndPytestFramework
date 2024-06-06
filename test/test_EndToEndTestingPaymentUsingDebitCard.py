from Pages.creditCardPaymentShopping import creditCard
def test_DebitCardPayment(browser):
    p1=creditCard(browser)
    p1.checkEndToEndTesting()