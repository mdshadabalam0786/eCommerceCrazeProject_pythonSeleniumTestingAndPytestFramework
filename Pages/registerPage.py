from lib.SeleniumWrapper import Basepage
from lib.excel_lib import loginLocator,registerLocator,registerData

class Register:
    createAccountXpath='//span[text()="Create Account"]'
    def __init__(self,driver):
        self.driver=driver

    def shopperRegister(self):
        loginLocators=loginLocator()
        regLoc=registerLocator()
        regDatas=registerData()
        sr1=Basepage(self.driver)
        sr1.clickElement((loginLocators[0][0],loginLocators[0][1])) # this xpath from loginPage
        sr1.clickElement((regLoc[0][0],regLoc[0][1]))
        sr1.sendKyeElement((regLoc[1][0],regLoc[1][1]),regDatas[0][0])
        sr1.sendKyeElement((regLoc[2][0],regLoc[2][1]),regDatas[0][1])
        if regDatas[0][2]=='male':
           sr1.clickElement((regLoc[3][0],regLoc[3][1]))  
        elif regDatas[0][2]=='female':
            sr1.clickElement(("xpath",'//input[@id="Female"]'))
        else:
            sr1.clickElement(("xpath",'//input[@id="Other"]'))
        sr1.sendKyeElement((regLoc[4][0],regLoc[4][1]),regDatas[0][3])
        sr1.sendKyeElement((regLoc[5][0],regLoc[5][1]),regDatas[0][4]) 
        sr1.sendKyeElement((regLoc[6][0],regLoc[6][1]),regDatas[0][5]) 
        sr1.sendKyeElement((regLoc[7][0],regLoc[7][1]),regDatas[0][6]) 
        sr1.clickElement((regLoc[8][0],regLoc[8][1]))
        self.driver.get_screenshot_as_file(r"D:\scapper\ShoppersStackProject1\Screenshortfolder\shopperRegister.png")
        sr1.clickElement((regLoc[9][0],regLoc[9][1]))
        
        
