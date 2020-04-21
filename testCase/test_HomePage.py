from selenium import webdriver
import time
import pytest
#===============================================================================================
    
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
#===============================================================================================
# 1) Click on hotels 
# 2) search for city
# 3) validate that 20 hotels are displayed in results

def test_click_hotel():
    hotel = driver.find_element_by_id('primary-header-hotel').click()

def test_find_city():
    ser_city = driver.find_element_by_xpath("//input[@id='hotel-destination-hlp']").send_keys('Dallas')

def test_Dallas_click():
    driver.find_element_by_xpath('//*[@id="aria-option-0"]/div[2]/strong').click()

def test_search_button():
    driver.find_element_by_xpath('//*[@id="gcw-hotel-form-hlp"]/div[13]/label/button').click()

def test_hotels():
    number_of_hotels = len(driver.find_elements_by_xpath("//section[@class='results']/ol/li"))
    # print('Numbers of hotles: ',number_of_hotels)

    assert number_of_hotels > 21
    driver.back()   
#===============================================================================================
    
# Go to main page
# Click on Hotels
# Search for ^&$(^%&$)(&*^
# Verify that "Sorry, we're having problem on our end" is displayed
# Verify that "Try again" button is visible and its state enabled
