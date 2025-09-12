from conf import Conf
from utils.page_utils import PageUtils
from locators.account_page_locators import AccountPageLocators
from utils.steps import Steps

class TestAccountPage:    
    def blocked_test_account_page_without_cred_is_redirect_to_login(self, page_utils: PageUtils):
        # в данный момент прямой переход на account page не возможен (даже если уже залогинены)
        page_utils.driver.get(Conf.ACCOUNT_PAGE) 
        page_utils.is_element_not_present(AccountPageLocators.LOGOUT_BUTTON)
        
    def test_logout(self, steps: Steps, page_utils: PageUtils):
        steps.login(Conf.EMAIL, Conf.PASSWORD)
        steps.logout()
