from EXProject.page_objects.home import HotelButton
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import pytest


@pytest.mark.usefixtures("setup")
class TestHotels():

    # @pytest.mark.skip
    @pytest.mark.negative_scenario
    def test_hotel_search_negative(self, setup):
        self.hp = HotelButton(setup)
        time.sleep(3)
        self.hp.click_hotel_btn()
        self.hp.enter_hotel_city("^&$(^%&$)(&*^")
        self.hp.click_search_btn()
        time.sleep(3)
        assert self.hp.verify_try_again_enabled() == True

    # @pytest.mark.skip
    @pytest.mark.positive_scenario
    def test_search_hotel(self, setup):
        self.hp = HotelButton(setup)
        time.sleep(1.5)
        self.hp.click_hotel_btn()
        self.hp.enter_hotel_city("Dallas")
        self.hp.click_search_btn()
