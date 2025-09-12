from utils.steps import Steps
from conf import Conf

class TestLoginPage:
    def test_login_success(self, steps: Steps):
        steps.login(Conf.EMAIL, Conf.PASSWORD)
