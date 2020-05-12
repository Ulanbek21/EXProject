import time
import pytest
from EXProject.page_objects.home import LoginPage
from EXProject.utilities.util import Screenshot
import pdb


@pytest.mark.usefixtures("setup")
class TestLogin():
    
    def test_login(self, setup):
        # logging.info(' info log  for test_flights... ') # 1 
        self.lg = LoginPage(setup)
        self.sc = Screenshot(setup)
        self.lg.account_btn()
        self.lg.sign_in_btn()
        self.lg.mail_adr('Shaidulaev@mail.ru')
        self.lg.enter_psw('Ulanbek21')
        self.lg.sing_in_click()
        time.sleep(1)
        self.sc.take_screenshot()