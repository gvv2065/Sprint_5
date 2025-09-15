from locators.ingredients_locators import IngredientsLocators
from utils.page_utils import PageUtils 
from selenium.common.exceptions import TimeoutException

class IngredientsHelper:
    def __init__(self, page_utils: PageUtils):
        self.page_utils = page_utils

    def assert_tabs_navigation(self, tab_names):
        for tab_name in tab_names:
            try:
                tab_element = self.page_utils.find_clickable_element(IngredientsLocators.get_tab_base_locator(tab_name))
                tab_element.click()
                self.page_utils.find_element(IngredientsLocators.get_active_tab_locator(tab_name))
                self.page_utils.find_element(IngredientsLocators.get_section_header_locator(tab_name))
                return True
            except TimeoutException as e:
                raise AssertionError(f"Ошибка при проверке вкладки '{tab_name}': {str(e)}")
            except Exception as e:
                raise AssertionError(f"Непредвиденная ошибка при проверке вкладки '{tab_name}': {str(e)}")
