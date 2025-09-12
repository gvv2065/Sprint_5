import pytest
from conf import Conf
from utils.page_utils import PageUtils
from locators.forgot_password_locators import ForgotPasswordLocators

class TestForgotPasswordPage:
    @pytest.fixture(autouse=True)
    def before_each(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.FORGOT_PASSWORD_PAGE)
            
    def test_login_button_is_redirect_to_login_page(self, page_utils: PageUtils):
        page_utils.find_clickable_element(ForgotPasswordLocators.LOGIN_BUTTON).click()
        assert page_utils.driver.current_url == Conf.LOGIN_PAGE
