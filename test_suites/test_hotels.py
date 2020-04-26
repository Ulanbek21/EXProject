from selenium import webdriver
from EXProject.page_objects.home import HomePage
import time
import pytest


# Go to main page
# Click on Hotels
# Search for ^&$(^%&$)(&*^
# Verify that "Sorry, we're having problem on our end" is displayed
# Verify that "Try again" button is visible and its state enabled




class TestHotels():

    @pytest.mark.negative_scenario
    @pytest.mark.usefixtures("setup")
    def test_hotel_search_negative(self, setup):
        hp = HomePage(setup)
        hp.click_hotel_btn()
        hp.enter_hotel_city("^&$(^%&$)(&*^")
        hp.click_search_btn()
        time.sleep(3)
        assert hp.verify_try_again_enabled() == True
