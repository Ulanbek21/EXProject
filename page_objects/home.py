from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
import time
import pytest
import pdb


class HomePage():


    def __init__(self, driver):
        self.driver = driver


# Actions

#------------------------------------------------------------------------------Flight


class FlightButton:

    def __init__(self, driver):
        self.driver = driver


    _returning_fld_id = "flight-returning-flp"
    _departing_fld_id = "flight-departing-flp"

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
    


#------------------------------------------------------------------------------Hotel
class HotelButton:

    def __init__(self, driver):
        self.driver = driver


    # transforms a method into attribute (in simple words - treat it like a variable [element = driver.find...])
    @property
    def hotel_btn(self):
        elem = self.driver.find_element_by_css_selector(
            '#primary-header-hotel')
        return elem  # outcome is the same as [hotel_btn = elem variable]

    @property
    def try_again_btn(self):
        try_again_btn = self.driver.find_element_by_xpath(
            "//span[contains(text(),'Try again')]")
        return try_again_btn

    @property
    def dropdown_close_btn(self):
        elem = self.driver.find_elements_by_css_selector("a.close")
        # pdb.set_trace()
        if len(elem) == 2:
            return elem[1]
        else:
            return None

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

    def verify_try_again_enabled(self):
        return self.try_again_btn.is_enabled()

#--------------------------------------------------------------------Cars


class CarsButoon:

    def __init__(self, driver):
        self.driver = driver


    def click_cars_btn(self):
        self.driver.find_element_by_id('primary-header-car').click()

    def picking_up(self,keyword):
        elem = self.driver.find_element_by_id('car-pickup-clp')
        elem.click()
        elem.send_keys(keyword)

    def dropdown_close_btn(self):
        elem = self.driver.find_element_by_xpath("//a[contains(text(),'Close')]")
        elem.click()

    def dropping_off(self,keyword):
        elem = self.driver.find_element_by_xpath("//input[@id='car-dropoff-clp']")
        elem.click()
        elem.send_keys(keyword)

    def pick_up_date(self,keyword):
        elem = self.driver.find_element_by_id('car-pickup-date-clp')
        elem.click()
        elem.send_keys(keyword)

    def pick_up_time(self,keyword):
        elem = self.driver.find_element_by_id('car-pickup-time-clp')
        elem.click()
        elem.send_keys(keyword)

    def drop_off_date(self,keyword):
        elem = self.driver.find_element_by_id('car-dropoff-date-clp')
        elem.click()
        elem.send_keys(keyword)

    def drop_off_time(self,keyword):
        elem = self.driver.find_element_by_name('time2')
        elem.click()
        elem.send_keys(keyword)


    def click_search_button(self):
        self.driver.find_element_by_id('gcw-submit-car').click()
    
    def number_off_cars(self):
        elements = len(self.driver.find_elements_by_xpath("//div[@id='search-results']/div/div/div"))
        print('Total number of cars: ',elements)



#--------------------------------------------------------------------Login
class LoginPage():


    def __init__(self, driver):
        self.driver = driver

    def account_btn(self):
        self.driver.find_element_by_id('header-account-menu').click()

    def sign_in_btn(self):
        self.driver.find_element_by_id('account-signin').click()
    
    def mail_adr(self,keyword):
        el = self.driver.find_element_by_id('gss-signin-email')
        el.click()
        time.sleep(0.5)
        el.send_keys(keyword)

    def enter_psw(self,keyword):
        pwd = self.driver.find_element_by_id('gss-signin-password')
        pwd.click()
        time.sleep(0.5)
        pwd.send_keys(keyword)

    def sing_in_click(self):
        self.driver.find_element_by_xpath('//*[@id="gss-signin-submit"]').click()