from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
import time
import pytest
import pdb


class HomePage():


    def __init__(self, driver):
        self.driver = driver

    # Locators

    _returning_fld_id = "flight-returning-flp"
    _departing_fld_id = "flight-departing-flp"

    # Elements

    @property
    def departing_fld(self):
        element = self.driver.find_element_by_id(
            self._departing_fld_id)
        return element

    @property
    def returning_fld(self):
        element = self.driver.find_element_by_id(
            self._returning_fld_id)
        return element

    @property
    def try_again_btn(self):
        try_again_btn = self.driver.find_element_by_xpath(
            "//span[contains(text(),'Try again')]")
        return try_again_btn

    # transforms a method into attribute (in simple words - treat it like a variable [element = driver.find...])
    @property
    def hotel_btn(self):
        elem = self.driver.find_element_by_css_selector(
            '#primary-header-hotel')
        return elem  # outcome is the same as [hotel_btn = elem variable]

    @property
    def dropdown_close_btn(self):
        elem = self.driver.find_elements_by_css_selector("a.close")
        # pdb.set_trace()
        if len(elem) == 2:
            return elem[1]
        else:
            return None


# Actions

    def verify_try_again_enabled(self):
        return self.try_again_btn.is_enabled()

    def click_hotel_btn(self):
        self.hotel_btn
        self.hotel_btn.click()
        # time.sleep(1)
        # self.driver.execute_script("window.scrollBy(0,300)","") # <-------------------------

    def enter_hotel_city(self, keyword):
        elem = self.driver.find_element_by_xpath(
            "//input[@id='hotel-destination-hlp']")
        elem.click()
        elem.send_keys(keyword)
        time.sleep(2)

    def click_search_btn(self):
        if self.dropdown_close_btn is not None:
            self.driver.execute_script(
                "arguments[0].scrollIntoViewIfNeeded();", self.dropdown_close_btn)
            time.sleep(2)
            self.dropdown_close_btn.click()
        else:
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
