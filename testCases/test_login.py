from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadCOnfig

class Test_001_Login:
    baseUrl = ReadCOnfig.getApplicationUrl()
    username = ReadCOnfig.getUseremail()
    password = ReadCOnfig.getPassword()


    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title =self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            assert False