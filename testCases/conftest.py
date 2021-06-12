from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="/Users/johnpaolopaulino/Downloads/Web_driver/chromedriver")
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="/Users/johnpaolopaulino/Downloads/Web_driver/geckodriver")
        print("Launching Firefox browser")
    # else:
    #     driver = webdriver.Ie()
    return driver

def pytest_addoption(parser): # this will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return the Browser value to setup method
    return request.config.getoption("--browser")