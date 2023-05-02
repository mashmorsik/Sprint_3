from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestTransitions:

    def test_from_profile_to_constructor_with_constructor_button(self, logged_in_user):
        driver = logged_in_user
        driver.find_element(*Locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
        driver.find_element(*Locators.LOCATOR_CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.LOCATOR_MAKE_ORDER_BUTTON), \
            'Не отработал переход из личного кабинета в конструктор по клику на "Конструктор"'

    def test_from_profile_to_constructor_with_logo(self, logged_in_user):
        driver = logged_in_user
        driver.find_element(*Locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
        driver.find_element(*Locators.LOCATOR_LOGO).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_MAKE_ORDER_BUTTON))
        assert driver.find_element(*Locators.LOCATOR_MAKE_ORDER_BUTTON), \
            'Не отработал переход из личного кабинета в конструктор по клику на логотип'

    def test_go_to_profile_page_from_main_page(self, logged_in_user):
        driver = logged_in_user
        driver.find_element(*Locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_PROFILE_BUTTON))
        assert driver.find_element(*Locators.LOCATOR_PROFILE_BUTTON), \
            'Не отработал переход в личный кабинет по клику на "Личный кабинет"'
