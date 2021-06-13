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


## Pytest HTML Report ##
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['MOdule Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
