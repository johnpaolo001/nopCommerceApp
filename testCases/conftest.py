from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="/Users/johnpaolopaulino/Downloads/Web_driver/chromedriver")
    return driver
