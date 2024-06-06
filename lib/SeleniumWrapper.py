from time import sleep

class Basepage:
    def __init__(self,driver):
        self.driver=driver
        
    def clickElement(self,locator):
       self.driver.find_element(*locator).click()
       sleep(5)
    
   
    def sendKyeElement(self,locator,value):
       self.driver.find_element(*locator).send_keys(value)
       sleep(5)






