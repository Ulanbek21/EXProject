from selenium import webdriver
import time
import pytest

#==============================================================================================
url = 'https://www.expedia.com/'
driver = webdriver.Chrome()

@pytest.mark.TC1
@pytest.mark.TC2
@pytest.mark.TC3
def test_HomePage():
    driver.get(url)
    driver.implicitly_wait(20)
    driver.maximize_window()
    assert driver.title == 'Expedia Travel: Search Hotels, Cheap Flights, Car Rentals & Vacations'
#===========================================   TC1   ====================================================
@pytest.mark.TC1
def test_click_hotel():
    hotel = driver.find_element_by_id('primary-header-hotel').click()

@pytest.mark.TC1
def test_find_city():
    ser_city = driver.find_element_by_xpath("//input[@id='hotel-destination-hlp']").send_keys('Dallas')

@pytest.mark.TC1
def test_search_button():
    driver.find_element_by_xpath('//*[@id="gcw-hotel-form-hlp"]/div[13]/label/button').click()

@pytest.mark.TC1
def test_hotels():
    number_of_hotels = len(driver.find_elements_by_xpath("//section[@class='results']/ol/li"))
    # print('Numbers of hotles: ',number_of_hotels)

    assert number_of_hotels > 10
    driver.back()   

#============================================    TC2    ===================================================
@pytest.mark.TC2
def test_Click_Hotel():
    driver.find_element_by_xpath("//a[@id='primary-header-hotel']").click()

@pytest.mark.TC2
def test_search():
    driver.find_element_by_xpath("//input[@id='hotel-destination-hlp']").clear() 
    driver.find_element_by_xpath("//input[@id='hotel-destination-hlp']").send_keys("^&$(^%&$)(&*^")

@pytest.mark.TC2
def test_click_search():
    driver.find_element_by_xpath('//*[@id="gcw-hotel-form-hlp"]/div[13]/label/button').click()

@pytest.mark.TC2   
def test_ok_button():
    ok = driver.find_element_by_xpath("//span[contains(text(),'Try again')]")   
    time.sleep(2)
    driver.back() 

#============================================    TC3    ===================================================

@pytest.mark.TC3
def test_flights():
    flight = driver.find_element_by_xpath("//a[@id='primary-header-flight']")
    flight.click()
    driver.refresh()
    time.sleep(2)


@pytest.mark.TC3
def test_cal():
    driver.find_element_by_id("flight-departing-flp").send_keys('04/05/2021')
    time.sleep(2)


@pytest.mark.TC3
def test_cal2():
    driver.find_element_by_id("flight-returning-flp").send_keys('05/05/2021')

