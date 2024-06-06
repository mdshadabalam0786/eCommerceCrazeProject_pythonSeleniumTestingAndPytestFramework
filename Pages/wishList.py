from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from lib.SeleniumWrapper import Basepage
from Pages.loginPage import Login
class Wislist:
    def __init__(self,browser):
        self.driver=browser

    def addWishList(self):
        p1=Login(self.driver)
        callBase=Basepage(self.driver)
        p1.loginShoppers()
        actions=ActionChains(self.driver)
        mensearch=self.driver.find_element("xpath",'//a[@id="men"]')
        actions.move_to_element(mensearch).perform()
        mensearch.click()
        sleep(10)

        searchBytshirt=self.driver.find_element("xpath",'//a[text()="T-shirts"]') 
        actions.move_to_element(searchBytshirt).perform()
        searchBytshirt.click() 
        sleep(5)

        searchmen=self.driver.find_element("xpath",'(//a[text()="Men"])[2]') 
        actions.move_to_element(searchmen).perform()
        
        sleep(5)
  
        wishSearch=self.driver.find_element("xpath","((//div[@class='featuredProducts_footerRight__k498x'])[1]//*)[4]")
        actions.move_to_element(wishSearch).perform()
        wishSearch.click() 
        sleep(10)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', '//button[@aria-label="Account settings"]'))).click()
        sleep(3)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', '(//li[contains(@class,"MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters css-1km1ehz")])[2]'))).click()
        sleep(13)
