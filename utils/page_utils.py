from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException

class PageUtils:
    @property
    def driver(self):
        return self._driver
    
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def find_element(self, locator, timeout=10, condition=EC.presence_of_element_located):
        try:
            return WebDriverWait(self.driver, timeout).until(
                condition(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Элемент не найден: {locator}")

    def find_clickable_element(self, locator, timeout=10):
        try:
            return self.find_element(locator, timeout, EC.element_to_be_clickable)
        except TimeoutException:
            raise TimeoutException(f"Элемент не найден: {locator}")
    
    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.current_url == expected_url
        )
        current_url = self.driver.current_url
        assert current_url == expected_url
        
    def is_element_not_present(self, locator):
        elements = self.driver.find_elements(*locator)
        assert len(elements) == 0
    
    def is_element_present(self, locator):
        elements = self.driver.find_elements(*locator)
        assert len(elements) == 1
