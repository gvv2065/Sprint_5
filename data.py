class Conf:
    HOST = "https://stellarburgers.nomoreparties.site"
    EMAIL = "vitaliigr_31qafs_047@ya.ru"
    PASSWORD = "DUDwVu"
    MAIN_PAGE = HOST + "/"
    REGISTER_PAGE = HOST + "/register"
    LOGIN_PAGE = HOST + "/login"
    FORGOT_PASSWORD_PAGE = HOST + "/forgot-password"
    ACCOUNT_PAGE = HOST + "/account/profile"

class IngredientsData:
    TABS = {
        "СОУСЫ": "Соусы",
        "БУЛКИ": "Булки",
        "НАЧИНКИ": "Начинки",
    }
    ACTIVE_TAB_CLASS_NAME = 'tab_type_current'