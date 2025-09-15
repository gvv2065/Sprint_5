from utils.steps import Steps
from data import Conf

class TestLoginPage:
    def test_login_success(self, steps: Steps):
        isLoginSuccessful = steps.login(Conf.EMAIL, Conf.PASSWORD)
        assert isLoginSuccessful == True
