import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


@pytest.mark.usefixtures('correct_user')
def test_log_out_from_user_profile(correct_user):
    driver = webdriver.Chrome()
    driver.get(locators.MAIN_PAGE_URL)
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
    driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
    driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_PROFILE_PAGE_BUTTON))
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_LOGOUT_BUTTON))
    driver.find_element(*locators.LOCATOR_LOGOUT_BUTTON).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_LOGIN_HEADER))
    assert driver.find_element(*locators.LOCATOR_LOGIN_HEADER)
    driver.quit()
