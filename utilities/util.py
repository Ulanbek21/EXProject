
import pytest
import logging


class Logger:

    def generate_logs(self, level, message):
        """ 
            Levels\n
            1 = Critical\n
            2 = Error\n
            3 = Warning\n
            4 = Info\n
            5 = Debug\n
        """

        logging.basicConfig(filename="mylogs.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p'
                    )

        logging.basicConfig(filename='mylogs.log')
        logging.getLogger().setLevel(logging.INFO)



class Screenshot:

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self):
        self.driver.get_screenshot_as_file("screenshots/as_file.png") # 1) Approach
        #self.driver.save_screenshot("screenshots/save.png")       # 2) Approach


class Alerts:

    def accept_alert(self):
        self.driver.switch_to_alert().accept() # close alert window using ok button

    def dismiss_alert(self):
        self.driver.switch_to_alert().dismiss() # close alert window using cancel button


class Report:

    def generate_report(self):
        pass
        # pytest -v -s --html=report.htmlte .\test_suites\test_hotels.py <---- For specific file
        # pytest --html=report.html <----- For  whole TCes
    
