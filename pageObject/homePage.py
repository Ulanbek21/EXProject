from selenium.webdriver.common.keys import Keys
# from EXProject.browser import Browser
import time
import pytest


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    # Elements

    @property
    def departing_fld(self):
        element = self.driver.find_element_by_id(
            "flight-departing-flp")
        return element

    @property
    def returning_fld(self):
        element = self.driver.find_element_by_id(
            "flight-returning-flp")
        return element


# Actions


    def click_hotel_btn(self):
        self.driver.find_element_by_id('primary-header-hotel').click()

    def enter_hotel_city(self, keyword):
        self.driver.find_element_by_xpath(
            "//input[@id='hotel-destination-hlp']").send_keys(keyword)

    def click_search_btn(self):
        self.driver.find_element_by_xpath(
            '//*[@id="gcw-hotel-form-hlp"]/div[13]/label/button').click()

    def click_flight_btn(self):
        self.driver.find_element_by_xpath(
            "//a[@id='primary-header-flight']").click()

    def enter_departing_date(self, keyword):
        self.departing_fld.send_keys(keyword)

    def enter_returning_date(self, keyword):
        elem = self.returning_fld
        elem.send_keys(Keys.CONTROL, 'a')
        elem.send_keys(Keys.DELETE)
        elem.send_keys(keyword)
