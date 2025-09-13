from utils.page_utils import PageUtils
from data import Conf
from locators.login_page_locators import LoginPageLocators
from locators.account_page_locators import AccountPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from locators.login_success_locators import LoginSuccessLocators
from locators.top_menu_locators import TopMenuLocators

class Steps:
    def __init__(self, pageUtils: PageUtils):
        self._pageUtils = pageUtils
        
    def login(self, email, password):
        self._pageUtils.driver.get(Conf.LOGIN_PAGE)
        self._pageUtils.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self._pageUtils.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self._pageUtils.find_clickable_element(LoginPageLocators.LOGIN_BUTTON).click()
        # считаем что мы успешно залогинились если есть кнопка "Оформить заказ"
        self._pageUtils.find_element(LoginSuccessLocators.ORDER_REQUEST)
        
    def logout(self):
        self._pageUtils.find_clickable_element(TopMenuLocators.ACCOUNT_LINK).click()
        self._pageUtils.find_clickable_element(AccountPageLocators.LOGOUT_BUTTON).click()
        self._pageUtils.wait_for_url(Conf.LOGIN_PAGE)
        self._pageUtils.find_clickable_element(LoginPageLocators.LOGIN_BUTTON)
        
        
    def register(self, name, email, password):
        self._pageUtils.driver.get(Conf.REGISTER_PAGE)
        # заполняем форму и сабмитим
        self._pageUtils.find_element(RegistrationPageLocators.NAME_FIELD).send_keys(name)
        self._pageUtils.find_element(RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        self._pageUtils.find_element(RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        self._pageUtils.find_clickable_element(RegistrationPageLocators.REGISTER_BUTTON).click()
        # ассертим логин
        self.login(email, password)
        