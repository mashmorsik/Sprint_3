from selenium.webdriver.common.by import By


class Locators:

    #Главная страница
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site'

    LOCATOR_PROFILE_PAGE_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]') #Личный Кабинет
    LOCATOR_CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]') #Кнопка Конструктор
    LOCATOR_LOGO = (By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]/a') #Лого
    LOCATOR_GO_TO_PROFILE_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]') #Кнопка Войти в аккаунт
    LOCATOR_MAKE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]') #Кнопка Оформить заказ

    #Главная страница. Соберите бургер
    LOCATOR_BREAD_TAB = (By.XPATH, './/span[text()="Булки"]')
    LOCATOR_SAUCE_TAB = (By.XPATH, './/span[text()="Соусы"]')
    LOCATOR_FILLING_TAB = (By.XPATH, './/span[text()="Начинки"]')
    LOCATOR_CHOSEN_TAB = (By.CLASS_NAME, 'tab_tab_type_current__2BEPc')

    #Страница регистрации
    SIGNUP_PAGE_URL = 'https://stellarburgers.nomoreparties.site/register'

    LOCATOR_NAME_FIELD = (By.XPATH, './/label[contains(text(),"Имя")]/following-sibling::input') #Поле Имя
    LOCATOR_EMAIL_FIELD = (By.XPATH, './/label[contains(text(),"Email")]/following-sibling::input') #Поле Email
    LOCATOR_PASSWORD_FIELD = (By.XPATH, './/label[contains(text(),"Пароль")]/following-sibling::input') #Поле Password
    LOCATOR_ENTER_BUTTON_LOGIN = (By.XPATH, './/button[text()="Войти"]') #Кнопка Войти
    LOCATOR_ENTER_LINK_LOGIN = (By.XPATH, './/a[text()="Войти"]') #Ссылка Войти
    LOCATOR_REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]') #Кнопка Зергистрироваться
    LOCATOR_INCORRECT_PASSWORD = (By.XPATH, './/p[text()="Некорректный пароль"]')
    LOCATOR_USER_EXISTS = (By.XPATH, './/p[text()="Такой пользователь уже существует"]')

    #Личный Кабинет
    LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'

    LOCATOR_PROFILE_BUTTON = (By.XPATH, './/a[text()="Профиль"]') #Профиль
    LOCATOR_LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]') #Выход
    LOCATOR_LOGIN_HEADER = (By.XPATH, './/h2[text()="Вход"]') #Название формы входа в аккаунт

    #Восстановить пароль
    LOCATOR_RESET_PASSWORD_LINK = (By.XPATH, './/a[text()="Восстановить пароль"]') #Ссылка Восстановить пароль
    LOCATOR_RESET_BUTTON = (By.XPATH, './/button[text()="Восстановить"]') #Кнопка Восстановить
    LOCATOR_SAVE_BUTTON = (By.XPATH, './/button[text()="Сохранить"]') #Кнопка Сохранить
