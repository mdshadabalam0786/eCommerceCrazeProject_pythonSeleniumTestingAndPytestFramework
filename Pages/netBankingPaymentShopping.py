from time import sleep
from datetime import datetime
from Pages.loginPage import Login
class NetBanking:
    def __init__(self,browser):
        self.driver=browser
    def checkEndToEndTesting(self):
       p1=Login(self.driver)
       p1.loginShoppers()
       sleep(10)

       self.driver.find_element('xpath','(//button[@id="addToCart"])[3]').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)

       self.driver.find_element('xpath','//a[@id="cart"]/.').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)

       self.driver.find_element('xpath','//span[text()="Buy Now"]').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)

       self.driver.find_element('xpath','//input[@id="39644"]').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)

       self.driver.find_element('xpath','//button[text()="Proceed"]').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)  
        
       self.driver.find_element('xpath','(//input[@name="radio-buttons-group"])[1]').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2) 

       self.driver.find_element('xpath','//button[text()="Proceed"]').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)
       
       iframe=self.driver.find_element('xpath','//iframe[@title="Netbanking"]')
       self.driver.switch_to.frame(iframe)
       sleep(3)

       self.driver.find_element('xpath','//input[@value="IDHC"]').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)

       self.driver.find_element('xpath','//button[text()="Submit"]').click()
       sleep(10)
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)

       iframeNet=self.driver.find_element('xpath','//iframe[@title="Netbanking Login"]')
       self.driver.switch_to.frame(iframeNet)
       sleep(3)

       self.driver.find_element('xpath','//input[@id="User ID"]').send_keys("alamsahdab786@gmail.com")
       sleep(3) 

       self.driver.find_element('xpath','//input[@id="Password"]').send_keys("9nvprzK")
       sleep(3)

       self.driver.find_element('xpath','//button[@id="Submit"]').click()
       sleep(10) 
       now=datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\RNetBankingScreenShort\RNetbanking{now.second}.png")
       sleep(2)
       
       
       