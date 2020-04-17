# # ----------------------------------Creatin Page Object Class-------------------------for Login Page

# # 1) Creat Class

# # 2) Locaters

# # 3) Constractor

# # 4) Actions

# # ------------------------------------------------------------------
from selenium import webdriver

# # 1) Creat Class

class LoginPage:


# # 2) Locaters

    demo_click_id = 'demo-toggle'
    textbox_username_id = 'account_id'
    textbox_password_id = 'password'
    click_login_id = 'loginbutton'
    click_logout_id = 'btnLogout'


# # 3) Constractor

    def __init__(self,driver):
        self.driver = driver
        
# # 4) Actions

    def clickDemoButton(self):
        self.driver.find_element_by_id(self.demo_click_id).click()

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.click_login_id).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.click_logout_id).click()


# Page Object class and constractor ready! Next step is go and cread TC


        