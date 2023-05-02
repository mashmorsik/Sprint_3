from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from urls import Urls
from data import CorrectUser


class TestLogIn:
    def test_log_in_from_main_page_profile_button(self, driver):
        driver.find_element(*Locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
        driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(CorrectUser.email)
        driver.find_element(*Locators.LOCATOR_PASSWORD_FIELD).send_keys(CorrectUser.password)
        driver.find_element(*Locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.LOCATOR_MAKE_ORDER_BUTTON), \
            'Не отработал вход через кнопку "Личный кабинет"'

    def test_log_in_from_main_page_go_to_profile_button(self, driver):
        driver.find_element(*Locators.LOCATOR_GO_TO_PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(CorrectUser.email)
        driver.find_element(*Locators.LOCATOR_PASSWORD_FIELD).send_keys(CorrectUser.password)
        driver.find_element(*Locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.LOCATOR_MAKE_ORDER_BUTTON), \
            'Не отработал вход по кнопке "Войти в аккаунт" на главной странице'

    def test_log_in_from_registration_page(self, driver):
        driver.get(Urls.SIGNUP_PAGE_URL)
        driver.find_element(*Locators.LOCATOR_ENTER_LINK_LOGIN).click()
        driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(CorrectUser.email)
        driver.find_element(*Locators.LOCATOR_PASSWORD_FIELD).send_keys(CorrectUser.password)
        driver.find_element(*Locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.LOCATOR_MAKE_ORDER_BUTTON), \
            'Не отработал вход через кнопку в форме регистрации'

    def test_log_in_forgot_password_button(self, driver):
        driver.find_element(*Locators.LOCATOR_GO_TO_PROFILE_BUTTON).click()
        driver.find_element(*Locators.LOCATOR_RESET_PASSWORD_LINK).click()
        driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(CorrectUser.email)
        driver.find_element(*Locators.LOCATOR_RESET_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_SAVE_BUTTON))
        assert driver.find_element(*Locators.LOCATOR_SAVE_BUTTON), \
            'Не отработал вход через кнопку в форме восстановления пароля'
