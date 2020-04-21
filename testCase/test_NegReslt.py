from selenium import webdriver
import time
import pytest


# Go to main page
# Click on Hotels
# Search for ^&$(^%&$)(&*^
# Verify that "Sorry, we're having problem on our end" is displayed
# Verify that "Try again" button is visible and its state enabled



url = 'https://www.expedia.com/'
driver = webdriver.Chrome()

def test_Home_Page():
    driver.get(url)
    driver.implicitly_wait(20)
    driver.maximize_window()
    assert driver.title == 'Expedia Travel: Search Hotels, Cheap Flights, Car Rentals & Vacations'

def test_click_hotel():
    hotel = driver.find_element_by_id('primary-header-hotel').click()

def test_find_city():
    ser_city = driver.find_element_by_name("destination")
    ser_city.send_keys('^&$(^%&$)(&*^')

def test_search_button():
    driver.find_element_by_xpath('//*[@id="gcw-hotel-form-hlp"]/div[13]/label/button').click()

def test_Try_Button():
    try_ag = driver.find_element_by_xpath("//span[contains(text(),'Try again')]")
    print('Display status of search button: ',try_ag.is_displayed())
    print('Enabled status of search button: ',try_ag.is_enabled())
    try_ag.click()