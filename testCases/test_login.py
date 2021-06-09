from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadCOnfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadCOnfig.getApplicationUrl()
    username = ReadCOnfig.getUseremail()
    password = ReadCOnfig.getPassword()

    logger = LogGen.loggen()


    def test_homePageTitle(self,setup):

        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home page title is passed **********")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home page title is failed **********")
            assert False

    def test_login(self,setup):
        self.logger.info("********** Verifying Login Test **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title =self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Login Test is passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("********** Login test is failed **********")
            assert False