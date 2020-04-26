
import time
import pytest
from EXProject.pageObject.homePage import HomePage
import pdb



@pytest.mark.usefixtures("setup")
class TestFlights():

    def test_flights(self):
        self.gt = HomePage()
        self.gt.click_flight_btn()
        self.time.sleep(2)
        self.gt.enter_departing_date('05/12/2020')
        # pdb.set_trace() 
        self.gt.enter_returning_date('05/20/2020')
        self.gt.quit_browser()
