import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


@pytest.mark.usefixtures('correct_user', 'incorrect_password_user', 'incorrect_email_user')
class TestSignUp:

    def test_successful_registration_with_correct_name_email_password(self, correct_user):
        driver = webdriver.Chrome()
        driver.get(locators.SIGNUP_PAGE_URL)
        driver.find_element(*locators.LOCATOR_NAME_FIELD).send_keys(
            correct_user.get('name'))
        driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
        driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
        driver.find_element(*locators.LOCATOR_REGISTRATION_BUTTON).click()
        driver.find_element(*locators.LOCATOR_ENTER_LINK_LOGIN).click()
        WebDriverWait(driver, 8)
        driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
        driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
        driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(locators.LOCATOR_PROFILE_PAGE_BUTTON))
        driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/input[@value="Евгений"]')))
        assert driver.find_element(By.XPATH, './/input[@value="Евгений"]')
        driver.quit()

    def test_sign_up_incorrect_password(self, incorrect_password_user):
        driver = webdriver.Chrome()
        driver.get(locators.SIGNUP_PAGE_URL)
        driver.find_element(*locators.LOCATOR_NAME_FIELD).send_keys(incorrect_password_user.get('name'))
        driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(incorrect_password_user.get('email'))
        driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(incorrect_password_user.get('password'))
        driver.find_element(*locators.LOCATOR_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(locators.LOCATOR_INCORRECT_PASSWORD))
        assert driver.find_element(*locators.LOCATOR_INCORRECT_PASSWORD)
        driver.quit()

    def test_sign_up_incorrect_email(self, incorrect_email_user):
        driver = webdriver.Chrome()
        driver.get(locators.SIGNUP_PAGE_URL)
        driver.find_element(*locators.LOCATOR_NAME_FIELD).send_keys(incorrect_email_user.get('name'))
        driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(incorrect_email_user.get('email'))
        driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(incorrect_email_user.get('password'))
        driver.find_element(*locators.LOCATOR_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(locators.LOCATOR_USER_EXISTS))
        assert driver.find_element(*locators.LOCATOR_USER_EXISTS)
        driver.quit()
