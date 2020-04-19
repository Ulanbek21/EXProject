
import pytest
from selenium import webdriver



@pytest.fixture()
def setUp():
    driver = webdriver.Chrome()
    yield
    driver.quit()
    
# This method will get value from CLI(comman line interfeis) /////  HOOKS
# pytest -v -s --html=report.html pytestTests\CommandLine\test_CommandLine.py  --driver  chrome
# def pytest_addoption(parser):
#     parser.addoption('--driver')

# # This method we need to write on emore fixture method
# @pytest.fixture()
# def driver(request):# This will return the driver value to set up method
#     return request.config.getoption('--driver')