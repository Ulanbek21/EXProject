import time
import pytest
from EXProject.page_objects.home import CarsButoon
from EXProject.utilities.util import Screenshot
import pdb


@pytest.mark.usefixtures("setup")
class TestCars():
    
    def test_cars(self, setup):
        # logging.info(' info log  for test_flights... ') # 1 
        self.hp = CarsButoon(setup)
        self.sc = Screenshot(setup)
        self.hp.click_cars_btn()
        self.hp.picking_up('New York')
        time.sleep(1)
        self.hp.dropdown_close_btn()
        self.hp.dropping_off('California')
        time.sleep(1)
        self.hp.dropdown_close_btn()
        self.hp.pick_up_date('09/10/2020')
        self.hp.pick_up_time('7:00 am')
        self.sc.take_screenshot()
        self.hp.drop_off_date('10/10/2020')
        self.hp.drop_off_time('11:00 am')
        time.sleep(1)
        self.hp.click_search_button()
        self.hp.number_off_cars()
        

        
