import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators


@pytest.mark.usefixtures('correct_user')
def test_from_profile_to_constructor_with_constructor_button(correct_user):
    driver = webdriver.Chrome()
    driver.get(locators.MAIN_PAGE_URL)
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
    driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
    driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_PROFILE_PAGE_BUTTON))
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_MAKE_ORDER_BUTTON))
    assert driver.find_element(*locators.LOCATOR_MAKE_ORDER_BUTTON)
    driver.quit()


def test_from_profile_to_constructor_with_logo(correct_user):
    driver = webdriver.Chrome()
    driver.get(locators.MAIN_PAGE_URL)
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
    driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
    driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_PROFILE_PAGE_BUTTON))
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_LOGO).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_MAKE_ORDER_BUTTON))
    assert driver.find_element(*locators.LOCATOR_MAKE_ORDER_BUTTON)
    driver.quit()