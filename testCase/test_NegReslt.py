from selenium import webdriver
from EXProject.pageObject.homePage import HomePage
import time
import pytest


# Go to main page
# Click on Hotels
# Search for ^&$(^%&$)(&*^
# Verify that "Sorry, we're having problem on our end" is displayed
# Verify that "Try again" button is visible and its state enabled


url = 'https://www.expedia.com/'
driver = webdriver.Chrome()
hp = HomePage(driver)  # create new object for MainPage class to instantiate


def test_Home_Page():
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    assert driver.title == 'Expedia Travel: Search Hotels, Cheap Flights, Car Rentals & Vacations'


def test_hotel_search_negative():
    hp.click_hotel_btn()
    hp.enter_hotel_city("^&$(^%&$)(&*^")
    hp.click_search_btn()
    time.sleep(3)
    try_ag = driver.find_element_by_xpath(
        "//span[contains(text(),'Try again')]")
    # print(try_ag.is_displayed())
    # print(try_ag.is_enabled())
    assert try_ag.is_displayed() == True
    assert try_ag.is_enabled() == True
