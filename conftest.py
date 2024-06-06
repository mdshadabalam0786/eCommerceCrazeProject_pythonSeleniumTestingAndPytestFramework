import pytest


from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.webdriver import WebDriver as edge

def pytest_addoption(parser):
    parser.addoption("--browser_name")
    parser.addoption("--env")


@pytest.fixture()
def env_config(request):
	env_ = request.config.getoption("--env")

	if env_.lower() == "test":
		print("openning in test environment===============")
		return TestConfigurations()
	elif env_.lower() == "stage":
		print("openning in stage environment============")
		return StageConfigurations()
	

@pytest.fixture(scope="function")
def browser(request,env_config):
    browser_=request.config.getoption("--browser_name")
    if browser_.lower()=="chrome":
            print("openning the chrome browser==========")
            driver=WebDriver()

    elif browser_.lower()=="edge":
         print("openning the edge browser===========")
         driver=edge()
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get(env_config.url)
    sleep(20)
    yield driver
    print("Closing Browser")
    driver.close()

class TestConfigurations():
	url = "https://www.shoppersstack.com/"
	


class StageConfigurations():
	url = "https://www.shoppersstack.com/"
	
