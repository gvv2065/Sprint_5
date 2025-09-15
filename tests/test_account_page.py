from data import Conf
from utils.steps import Steps

class TestAccountPage:
    def test_logout(self, steps: Steps):
        steps.login(Conf.EMAIL, Conf.PASSWORD)
        isLogoutSuccessful = steps.logout()
        assert isLogoutSuccessful == True
