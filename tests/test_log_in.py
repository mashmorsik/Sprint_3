import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


@pytest.mark.usefixtures('correct_user')
class TestLogIn:
    def test_log_in_from_main_page_account_button(self, correct_user):
        driver = webdriver.Chrome()
        driver.get(locators.MAIN_PAGE_URL)
        driver.find_element(*locators.LOCATOR_GO_TO_PROFILE_BUTTON).click()
        driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
        driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
        driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(locators.LOCATOR_MAKE_ORDER_BUTTON))
        assert driver.find_element(*locators.LOCATOR_MAKE_ORDER_BUTTON)
        driver.quit()

    def test_log_in_from_main_page_profile_button(self, correct_user):
        driver = webdriver.Chrome()
        driver.get(locators.MAIN_PAGE_URL)
        driver.find_element(*locators.LOCATOR_GO_TO_PROFILE_BUTTON).click()
        driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
        driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
        driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(locators.LOCATOR_MAKE_ORDER_BUTTON))
        assert driver.find_element(*locators.LOCATOR_MAKE_ORDER_BUTTON)
        driver.quit()

    def test_log_in_from_registration_page(self, correct_user):
        driver = webdriver.Chrome()
        driver.get(locators.SIGNUP_PAGE_URL)
        driver.find_element(*locators.LOCATOR_ENTER_LINK_LOGIN).click()
        driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
        driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
        driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(locators.LOCATOR_MAKE_ORDER_BUTTON))
        assert driver.find_element(*locators.LOCATOR_MAKE_ORDER_BUTTON)
        driver.quit()

    def test_log_in_forgot_password_button(self, correct_user):
        driver = webdriver.Chrome()
        driver.get(locators.MAIN_PAGE_URL)
        driver.find_element(*locators.LOCATOR_GO_TO_PROFILE_BUTTON).click()
        driver.find_element(*locators.LOCATOR_RESET_PASSWORD_LINK).click()
        driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
        driver.find_element(*locators.LOCATOR_RESET_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(locators.LOCATOR_SAVE_BUTTON))
        assert driver.find_element(*locators.LOCATOR_SAVE_BUTTON)
        driver.quit()
