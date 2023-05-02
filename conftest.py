import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import CorrectUser
from locators import Locators


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1500,900")

    driver = webdriver.Chrome(options=options)
    driver.get(Locators.MAIN_PAGE_URL)

    yield driver
    driver.quit()


@pytest.fixture()
def logged_in_user(driver):
    driver.get(Locators.LOGIN_PAGE_URL)
    driver.find_element(*Locators.LOCATOR_EMAIL_FIELD).send_keys(CorrectUser.email)
    driver.find_element(*Locators.LOCATOR_PASSWORD_FIELD).send_keys(CorrectUser.password)
    driver.find_element(*Locators.LOCATOR_ENTER_BUTTON_LOGIN).click()
    WebDriverWait(driver, 8).until(
        expected_conditions.visibility_of_element_located(Locators.LOCATOR_MAKE_ORDER_BUTTON))
    return driver
