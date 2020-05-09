import pytest
from selenium import webdriver
import time


@pytest.fixture(scope='function')
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.get("https://www.expedia.com/")
    driver.implicitly_wait(10)
    # driver.maximize_window()
    request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()