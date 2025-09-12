import pytest
from conf import Conf
from utils.page_utils import PageUtils
from selenium.webdriver.common.by import By
from locators.top_menu_locators import TopMenuLocators

class TestMainPage:
    @pytest.fixture(autouse=True)
    def before_each(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.MAIN_PAGE)
    
    def test_ingredients_tab_navigation(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.HOST)
        isTabActiveClassName = 'tab_type_current'
        for section_name in [ "Соусы", "Булки", "Начинки"]:
            divTab = page_utils.find_element((By.XPATH, f"//span[text()='{section_name}']/ancestor::div[contains(@class, 'tab') and not(contains(@class, '{isTabActiveClassName}'))]"))
            divTab.click()
            page_utils.find_element((By.XPATH, f"//span[text()='{section_name}']/ancestor::div[contains(@class, '{isTabActiveClassName}')]"))
            page_utils.find_element((By.XPATH, f"//h2[text()='{section_name}']"))
            
    def test_account_button_is_redirect_to_login_page(self, page_utils: PageUtils):
        page_utils.find_clickable_element(TopMenuLocators.ACCOUNT_LINK).click()
        assert page_utils.driver.current_url == Conf.LOGIN_PAGE
