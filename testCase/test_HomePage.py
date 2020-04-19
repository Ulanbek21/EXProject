from selenium import webdriver
import time
import pytest
# from EXProject.pageObject.homePage import OpenBrowser



url = 'https://www.expedia.com/'
driver = webdriver.Chrome()

def test_Home_Page():
    driver.get(url)
    driver.implicitly_wait(20)
    driver.maximize_window()
    assert driver.title == 'Expedia Travel: Search Hotels, Cheap Flights, Car Rentals & Vacations'

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
    

# def hotels():
#     number_of_hotels = driver.find_elements_by_xpath("//div[@class='uitk-cell all-cell-3-4 all-x-gutter-six']")
#     print('Rows:',len(number_of_hotels))

# def cal():
#     cal_but = driver.find_element_by_id('hotels-check-in-btn').click()

time.sleep(5)

handles = driver.switch_to.window
def hotels():
    number_of_hotels = len(driver.find_elements_by_xpath("//div[@class='uitk-cell all-cell-3-4 all-x-gutter-six']"))
    # print('Rows:',len(number_of_hotels))

    
    