import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


@pytest.mark.usefixtures('correct_user')
def test_constructor_assert_on_bread_tab(correct_user):
    driver = webdriver.Chrome()
    driver.get(locators.MAIN_PAGE_URL)
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
    driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
    driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_CHOSEN_TAB))
    assert driver.find_element(*locators.LOCATOR_CHOSEN_TAB).text == 'Булки'
    driver.quit()


def test_constructor_from_bread_to_sauce(correct_user):
    driver = webdriver.Chrome()
    driver.get(locators.MAIN_PAGE_URL)
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
    driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
    driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_CHOSEN_TAB))
    driver.find_element(*locators.LOCATOR_SAUCE_TAB).click()
    assert driver.find_element(*locators.LOCATOR_CHOSEN_TAB).text == 'Соусы'
    driver.quit()


def test_constructor_from_sauce_to_filling(correct_user):
    driver = webdriver.Chrome()
    driver.get(locators.MAIN_PAGE_URL)
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
    driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
    driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_CHOSEN_TAB))
    driver.find_element(*locators.LOCATOR_FILLING_TAB).click()
    assert driver.find_element(*locators.LOCATOR_CHOSEN_TAB).text == 'Начинки'
    driver.quit()


def test_constructor_from_filling_to_bread(correct_user):
    driver = webdriver.Chrome()
    driver.get(locators.MAIN_PAGE_URL)
    driver.find_element(*locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
    driver.find_element(*locators.LOCATOR_EMAIL_FIELD).send_keys(correct_user.get('email'))
    driver.find_element(*locators.LOCATOR_PASSWORD_FIELD).send_keys(correct_user.get('password'))
    driver.find_element(*locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_CHOSEN_TAB))
    driver.find_element(*locators.LOCATOR_FILLING_TAB).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(locators.LOCATOR_CHOSEN_TAB))
    driver.find_element(*locators.LOCATOR_BREAD_TAB).click()
    assert driver.find_element(*locators.LOCATOR_CHOSEN_TAB).text == 'Булки'
    driver.quit()
