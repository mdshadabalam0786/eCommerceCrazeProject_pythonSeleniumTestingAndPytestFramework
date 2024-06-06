from time import sleep
from datetime import datetime
from Pages.loginPage import Login
class creditCard:
    def __init__(self,browser):
        self.driver=browser
    def checkEndToEndTesting(self):
       p1=Login(self.driver)
       p1.loginShoppers()
       sleep(10)
       now = datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\EndToEndCreditCardPayment\Validlogin{now.second}.png")
       print("=====================")
       self.driver.find_element('xpath','(//button[@id="addToCart"])[3]').click()
       sleep(10)
       now = datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\EndToEndCreditCardPayment\Validlogin{now.second}.png")
      
       self.driver.find_element('xpath','//a[@id="cart"]/.').click()
       sleep(10)
       now = datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\EndToEndCreditCardPayment\Validlogin{now.second}.png")
      
       self.driver.find_element('xpath','//span[text()="Buy Now"]').click()
       sleep(10)
       now = datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\EndToEndCreditCardPayment\Validlogin{now.second}.png")
      
       self.driver.find_element('xpath','//input[@id="39644"]').click()
       sleep(10) 
       now = datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\EndToEndCreditCardPayment\Validlogin{now.second}.png")
       
       self.driver.find_element('xpath','//button[text()="Proceed"]').click()
       sleep(10)  
       now = datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\EndToEndCreditCardPayment\Validlogin{now.second}.png")
      
       self.driver.find_element('xpath','//div[@class="payment_addCards__HkDMo"]//button[text()="Add Card"]').click()
       sleep(10) 
       now = datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\EndToEndCreditCardPayment\Validlogin{now.second}.png")
      
       self.driver.find_element('xpath','(//input[@name="radio-buttons-group"])[4]').click()  
       sleep(10)
#-------------------------------------------------------------------------------------------------------
       
       self.driver.find_element('xpath','(//div[@class="MuiFormControl-root MuiTextField-root css-i44wyl"]//input)[1]').send_keys('Shadaab')
       sleep(5)
       self.driver.find_element('xpath','(//div[@class="MuiFormControl-root MuiTextField-root css-i44wyl"]//input)[2]').send_keys('7445789612367284')
       sleep(5)
       self.driver.find_element('xpath','(//div[@class="MuiFormControl-root MuiTextField-root css-i44wyl"]//input)[3]').send_keys('5924')
       sleep(5)
       self.driver.find_element('xpath','(//div[@class="MuiFormControl-root MuiTextField-root css-i44wyl"]//input)[4]').send_keys('1')
       sleep(5)
       self.driver.find_element('xpath','(//div[@class="MuiFormControl-root MuiTextField-root css-i44wyl"]//input)[5]').send_keys('29')
       sleep(5)
       self.driver.find_element('xpath','(//div[@class="MuiFormControl-root MuiTextField-root css-i44wyl"]//input)[6]').send_keys('884')
       sleep(5) 
       now = datetime.now()
       self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\EndToEndCreditCardPayment\Validlogin{now.second}.png")
      
       self.driver.find_element('xpath','//button[text()="Add"]').click()
       sleep(2)
       