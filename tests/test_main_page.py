import pytest
from data import Conf
from utils.page_utils import PageUtils
from locators.top_menu_locators import TopMenuLocators
from helpers.ingredients_helper import IngredientsHelper
from data import IngredientsData

class TestMainPage:
    @pytest.fixture(autouse=True)
    def before_each(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.MAIN_PAGE)
    
    def test_ingredients_tab_navigation(self, page_utils: PageUtils):
        page_utils.driver.get(Conf.MAIN_PAGE)
        ingredients_helper = IngredientsHelper(page_utils)
        isAssertTabSuccess = ingredients_helper.assert_tabs_navigation(IngredientsData.TABS.values())
        assert isAssertTabSuccess == True
            
    def test_account_button_is_redirect_to_login_page(self, page_utils: PageUtils):
        page_utils.find_clickable_element(TopMenuLocators.ACCOUNT_LINK).click()
        assert page_utils.driver.current_url == Conf.LOGIN_PAGE
