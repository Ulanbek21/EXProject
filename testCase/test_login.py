import pytest
from selenium import webdriver
from NADEXProject.pageObject.LoginPage import LoginPage




class Test_001_Login:

    baseURL = 'https://demo.nadex.com/login?logout=true'
    username = 'Ulanbek'
    password = 'Shaidullaev'
    driver = webdriver.Chrome()


    def test_homePageTitile(self):
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == 'Login | Nadex':
            assert True
        else:
            assert False

    def test_login(self):
        self.driver.get(self.baseURL)
        self.lopage = LoginPage(self.driver)
        self.lopage.clickDemoButton()
        self.lopage.setUserName(self.username)
        self.lopage.setPassword(self.password)
        self.lopage.clickLogin()
        act_title = self.driver.title

        # self.lopage.clickLogout()
        self.driver.close()
        if act_title == 'Nadex.com':
            assert True
        else:
            assert False







 