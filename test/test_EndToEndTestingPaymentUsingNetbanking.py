from Pages.netBankingPaymentShopping import NetBanking
def test_netBanking(browser):
    p1=NetBanking(browser)
    p1.checkEndToEndTesting()