from selenium.webdriver.common.by import By
from data import IngredientsData
class IngredientsLocators:
    HEADER_LABEL = (By.XPATH, "//h1[text()='Соберите бургер']")
    
    @staticmethod
    def get_tab_base_locator(tab_name):
        return (By.XPATH, f"//span[text()='{tab_name}']/ancestor::div[contains(@class, 'tab') and not(contains(@class, '{IngredientsData.ACTIVE_TAB_CLASS_NAME}'))]")
        
    @staticmethod
    def get_active_tab_locator(tab_name):
        return (By.XPATH, f"//span[text()='{tab_name}']/ancestor::div[contains(@class, '{IngredientsData.ACTIVE_TAB_CLASS_NAME}')]")
        
    @staticmethod
    def get_section_header_locator(tab_name):
        return (By.XPATH, f"//span[text()='{tab_name}']/ancestor::div[contains(@class, '{IngredientsData.ACTIVE_TAB_CLASS_NAME}')]")
