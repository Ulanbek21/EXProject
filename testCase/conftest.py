
import pytest
from selenium import webdriver



@pytest.fixture()
def setup(browser):
    print('Launchig chrom browser')
    if browser =='chrome':
        driver = webdriver.Chrome()
        print('Launching chrome browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    return  driver
    
# This method will get value from CLI(comman line interfeis) /////  HOOKS
# pytest -v -s --html=report.html pytestTests\CommandLine\test_CommandLine.py  --browser  chrome
def pytest_addoption(parser):
    parser.addoption('--browser')

# This method we need to write on emore fixture method
@pytest.fixture()
def browser(request):# This will return the browser value to set up method
    return request.config.getoption('--browser')