from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from data import CorrectUser, IncorrectEmailUser, IncorrectPasswordUser


class TestSignUp:

    def test_successful_registration_with_correct_name_email_password(self, driver):
        driver.get(Locators.SIGNUP_PAGE_URL)
        driver.find_element(*Locators.LOCATOR_NAME_FIELD).send_keys(CorrectUser.name)
        driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(CorrectUser.email)
        driver.find_element(*Locators.LOCATOR_PASSWORD_FIELD).send_keys(CorrectUser.password)
        driver.find_element(*Locators.LOCATOR_REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.LOCATOR_ENTER_LINK_LOGIN).click()
        WebDriverWait(driver, 8)
        driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(CorrectUser.email)
        driver.find_element(*Locators.LOCATOR_PASSWORD_FIELD).send_keys(CorrectUser.password)
        driver.find_element(*Locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_PROFILE_PAGE_BUTTON))
        driver.find_element(*Locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_NAME_FIELD))
        name = driver.find_element(*Locators.LOCATOR_NAME_FIELD).get_attribute('value')
        assert name == 'Евгений', \
            'Успешная регстрация пользователя'

    def test_sign_up_incorrect_password(self, driver):
        driver.get(Locators.SIGNUP_PAGE_URL)
        driver.find_element(*Locators.LOCATOR_NAME_FIELD).send_keys(IncorrectPasswordUser.name)
        driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(IncorrectPasswordUser.email)
        driver.find_element(*Locators.LOCATOR_PASSWORD_FIELD).send_keys(IncorrectPasswordUser.password)
        driver.find_element(*Locators.LOCATOR_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_INCORRECT_PASSWORD))
        assert driver.find_element(*Locators.LOCATOR_INCORRECT_PASSWORD), \
            'Ошибка регистрации: неверный пароль'

    def test_sign_up_incorrect_email(self, driver):
        driver.get(Locators.SIGNUP_PAGE_URL)
        driver.find_element(*Locators.LOCATOR_NAME_FIELD).send_keys(IncorrectEmailUser.name)
        driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(IncorrectEmailUser.email)
        driver.find_element(*Locators.LOCATOR_PASSWORD_FIELD).send_keys(IncorrectEmailUser.password)
        driver.find_element(*Locators.LOCATOR_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_USER_EXISTS))
        assert driver.find_element(*Locators.LOCATOR_USER_EXISTS), \
            'Ошибка регистрации: неверный email'
