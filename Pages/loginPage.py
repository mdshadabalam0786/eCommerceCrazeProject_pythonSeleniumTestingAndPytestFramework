from time import sleep
from datetime import datetime
import openpyxl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.SeleniumWrapper import Basepage
from lib.excel_lib import loginLocator,getDataFromExcelValidLoginCredential



class Login:
    def __init__(self,browser):
        self.driver=browser
        
    def loginShoppers(self):
        p1=Basepage(self.driver)
        resultUserPassword=getDataFromExcelValidLoginCredential() #returning the generator of data where five rows are there
        header=next(resultUserPassword) #skipping the column name
        x,y=next(resultUserPassword) # unpacking the second record of username and password
 
        locatorList=loginLocator() #here getting the list of locator
        p1.clickElement((locatorList[0][0],locatorList[0][1]))
        p1.sendKyeElement((locatorList[1][0],locatorList[1][1]),x)
        
        p1.sendKyeElement((locatorList[2][0],locatorList[2][1]),y)
        self.driver.get_screenshot_as_file(r"D:\scapper\ShoppersStackProject1\Screenshortfolder\shopperLogin.png")
        p1.clickElement((locatorList[3][0],locatorList[3][1]))

    

    def checkWithFiveValidCredential(self):
        
        file_path = r"D:\scapper\ShoppersStackProject1\data\TestData.xlsx"  # Use forward slashes
        wb = openpyxl.load_workbook(file_path)
        ws = wb["Login"]
        for index,rows in enumerate(ws.iter_rows(values_only=True)):
          if index>=1: 
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', '//button[text()="Login"]'))).click() 
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', '//input[@id="Email"]'))).send_keys(rows[0])
            sleep(3)
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(('xpath', '//input[@id="Password"]'))).send_keys(rows[1])
            sleep(3)
            now = datetime.now()
            self.driver.get_screenshot_as_file(f"D:\scapper\ShoppersStackProject1\Screenshortfolder\FiveDifferentCredential\Validlogin{now.second}.png")
            sleep(1)
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', '//span[text()="Login"]'))).click()
            sleep(3)

            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', '//button[@aria-label="Account settings"]'))).click()
            sleep(3)
           
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(('xpath', '//li[text()="Logout"]'))).click()
            sleep(3)


