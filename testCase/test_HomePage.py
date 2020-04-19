from selenium import webdriver
import time
import pytest


def test_Home_Page():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://www.expedia.com/')
    assert driver.title == 'Expedia Travel: Search Hotels, Cheap Flights, Car Rentals & Vacations'