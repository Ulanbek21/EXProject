from selenium import webdriver




class MainPage:

    def __init__(self, driver):
            self.driver = driver

    def test_click_hotel(self):
        self.driver.find_element_by_id('primary-header-hotel').click()

    def test_find_city(self, keyword):
        self.driver.find_element_by_xpath("//input[@id='hotel-destination-hlp']").send_keys(keyword)

    def test_search_button(self):
        self.driver.find_element_by_xpath('//*[@id="gcw-hotel-form-hlp"]/div[13]/label/button').click()
