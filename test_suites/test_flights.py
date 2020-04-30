
import time
import pytest
from EXProject.page_objects.home import HomePage
import pdb

@pytest.mark.usefixtures("setup")
class TestFlights():

    def test_flights(self, setup):
        # logging.info(' info log  for test_flights... ') # 1 
        self.hp = HomePage(setup)
        self.hp.click_flight_btn()
        # logging.info(' info log  for clickin action... ')
        time.sleep(2)
        self.hp.enter_departing_date('05/12/2020')
        # logging.info(' info log  for entering date in callendar... ')
        # pdb.set_trace() 
        self.hp.enter_returning_date('05/20/2020')
        # logging.info(' info log  for entering date in callendar... ')
        time.sleep(2)

    @pytest.mark.negative_scenario
    def test_flights_negative(self, setup):
        self.hp = HomePage(setup)
        self.hp.click_flight_btn()
        time.sleep(2)
        self.hp.enter_departing_date('^%*&()')
        # pdb.set_trace() 
        self.hp.enter_returning_date('^&$(^*')
        time.sleep(2)