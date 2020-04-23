from selenium import webdriver
from EXProject.pageObject.homePage import MainPage
import time
import pytest


# Go to main page
# Click on Hotels
# Search for ^&$(^%&$)(&*^
# Verify that "Sorry, we're having problem on our end" is displayed
# Verify that "Try again" button is visible and its state enabled



url = 'https://www.expedia.com/'
driver = webdriver.Chrome()
hp = MainPage(driver) # create new object for MainPage class to instantiate

def test_Home_Page():
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    assert driver.title == 'Expedia Travel: Search Hotels, Cheap Flights, Car Rentals & Vacations'

def test_click_hotel():
    hp.test_click_hotel()

def test_find_city():
    hp.test_find_city("^&$(^%&$)(&*^")

def test_search_button():
    hp.test_search_button()
time.sleep(3)
def test_Try_Button():
    try_ag = driver.find_element_by_xpath("//span[contains(text(),'Try again')]")
    assert try_ag.is_displayed() == True
    assert try_ag.is_enabled() == False
