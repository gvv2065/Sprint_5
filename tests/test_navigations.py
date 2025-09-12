from conf import Conf
from utils.page_utils import PageUtils
from locators.top_menu_locators import TopMenuLocators
from locators.login_page_locators import LoginPageLocators
from utils.steps import Steps
from selenium.webdriver.common.by import By

class TestNavigation:    
    def test_navigate_from_main_page_to_account(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.MAIN_PAGE) 
        page_utils.find_clickable_element(TopMenuLocators.ACCOUNT_LINK).click()
        page_utils.find_clickable_element(LoginPageLocators.LOGIN_BUTTON)
        
    def test_navigate_from_account_to_constuctor_is_possible(self, steps: Steps, page_utils: PageUtils):
        steps.login(Conf.EMAIL, Conf.PASSWORD)
        page_utils.find_clickable_element(TopMenuLocators.ACCOUNT_LINK).click()
        page_utils.find_clickable_element(TopMenuLocators.CONSTRUCTOR_LINK).click()
        page_utils.find_element((By.XPATH, "//h1[text()='Соберите бургер']"))
        
    def test_constructor_click_open_constuctor_page(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.LOGIN_PAGE) 
        page_utils.find_clickable_element(TopMenuLocators.CONSTRUCTOR_LINK).click()
        page_utils.find_element((By.XPATH, "//h1[text()='Соберите бургер']"))
    
    def test_logo_click_redirect_to_main_page(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.LOGIN_PAGE) 
        page_utils.find_clickable_element(TopMenuLocators.LOGO).click()
        assert page_utils.driver.current_url == Conf.MAIN_PAGE+"/"
