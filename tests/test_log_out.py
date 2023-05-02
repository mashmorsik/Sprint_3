from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestLogOut:
    def test_log_out_from_user_profile(self, logged_in_user):
        driver = logged_in_user
        driver.find_element(*Locators.LOCATOR_PROFILE_PAGE_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_LOGOUT_BUTTON))
        driver.find_element(*Locators.LOCATOR_LOGOUT_BUTTON).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_LOGIN_HEADER))
        assert driver.find_element(*Locators.LOCATOR_LOGIN_HEADER), \
            'Не отработал выход по кнопке "Выйти" в личном кабинете'
