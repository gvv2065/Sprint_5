import pytest
from utils.utils import generate_email, generate_password
from locators.registration_page_locators import RegistrationPageLocators
from utils.steps import Steps
from utils.page_utils import PageUtils
from conf import Conf

class TestRegistrationPage:
    @pytest.fixture(autouse=True)
    def before_each(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.REGISTER_PAGE)
        
    def test_registration_successful(self, steps: Steps):
        steps.register("TestUser", generate_email(), generate_password())
       
    def test_registration_failed_with_invalid_password(self, page_utils: PageUtils):
        # заполняем форму
        page_utils.find_element(RegistrationPageLocators.NAME_FIELD).send_keys("test")
        page_utils.find_element(RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email())
        page_utils.find_element(RegistrationPageLocators.PASSWORD_FIELD).send_keys("123")
        # проверяем что ошибки нет и пробуем нажать зарегистировать
        page_utils.is_element_not_present(RegistrationPageLocators.ERROR_MESSAGE)
        page_utils.find_clickable_element(RegistrationPageLocators.REGISTER_BUTTON).click()
        # проверяем что ошибка появилась и мы остались на старой странице
        page_utils.is_element_present(RegistrationPageLocators.ERROR_MESSAGE)
        assert page_utils.driver.current_url == Conf.REGISTER_PAGE
        
    def test_login_button_is_redirect_to_login_page(self, page_utils: PageUtils):
        page_utils.find_clickable_element(RegistrationPageLocators.LOGIN_BUTTON).click()
        assert page_utils.driver.current_url == Conf.LOGIN_PAGE
        