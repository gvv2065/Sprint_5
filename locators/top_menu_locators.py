from selenium.webdriver.common.by import By

class TopMenuLocators:
    ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    