# Автотесты для сервиса Stellar Burgers
1. Основа для написания автотестов — фреймворк pytest и selenium.
2. Команда для запуска — pytest -v.

## Проверено
### [Страница "Регистрация"](./tests/test_registration_page.py)  
<li> Успешная регистрация <b>test_registration_successful()</b>
<li> Ошибка для некорректного пароля <b>test_registration_failed_with_invalid_password()</b>
<li> Вход через кнопку в форме регистрации <b>test_login_button_is_redirect_to_login_page()</b>
 
### [Страница "Вход"](./tests/test_login_page.py)
<li> Успешный логин <b>test_login_success()</b>

### [Страница "Главная"](./tests/test_main_page.py)
<li> Работают переходы к разделам: «Булки», «Соусы», «Начинки» <b>test_ingredients_tab_navigation()</b>  
<li> Вход через кнопку «Личный кабинет» <b>test_account_button_is_redirect_to_login_page()</b>  

### [Страница "Забыли пароль"](./tests/test_forgot_password_page.py)
<li> Вход через кнопку в форме восстановления пароля <b>test_login_button_is_redirect_to_login_page()</b>  

### [Страница "Аккаунт"](./tests/test_account_page.py)
<li> Выход по кнопке «Выйти» в личном кабинете <b>test_logout()</b>  

### [Навигация](./tests/test_navigations.py)
<li> Переход в личный кабинет <b>test_navigate_from_main_page_to_account()</b>  
<li> Переход из личного кабинета в конструктор <b>test_navigate_from_account_to_constuctor_is_possible()</b>  
<li> Переход по клику на «Конструктор» <b>test_constructor_click_open_constuctor_page()</b>  
<li> Переход по клику на логотип Stellar Burgers <b>test_logo_click_redirect_to_main_page()</b>  