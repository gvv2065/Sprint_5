import pytest
from selenium import webdriver
from utils.page_utils import PageUtils
from utils.steps import Steps

@pytest.fixture
def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    try:
        yield driver
    finally:
        driver.quit()

@pytest.fixture
def page_utils(setup_driver):
    return PageUtils(setup_driver)

@pytest.fixture
def steps(page_utils):
    return Steps(page_utils)
