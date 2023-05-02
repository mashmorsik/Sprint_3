from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestConstructor:
    def test_constructor_assert_on_bread_tab(self, logged_in_user):
        driver = logged_in_user
        assert driver.find_element(*Locators.LOCATOR_CHOSEN_TAB).text == 'Булки',\
            'В конструкторе открыт раздел "Булки"'

    def test_constructor_from_bread_to_sauce(self, logged_in_user):
        driver = logged_in_user
        driver.find_element(*Locators.LOCATOR_SAUCE_TAB).click()
        assert driver.find_element(*Locators.LOCATOR_CHOSEN_TAB).text == 'Соусы', \
            'Переход из раздела "Булки" в "Соусы" в конструкторе'

    def test_constructor_from_sauce_to_filling(self, logged_in_user):
        driver = logged_in_user
        driver.find_element(*Locators.LOCATOR_FILLING_TAB).click()
        assert driver.find_element(*Locators.LOCATOR_CHOSEN_TAB).text == 'Начинки', \
            'Переход из раздела "Соусы" в "Начинки" в конструкторе'

    def test_constructor_from_filling_to_bread(self, logged_in_user):
        driver = logged_in_user
        driver.find_element(*Locators.LOCATOR_FILLING_TAB).click()
        WebDriverWait(driver, 8).until(
            expected_conditions.visibility_of_element_located(Locators.LOCATOR_CHOSEN_TAB))
        driver.find_element(*Locators.LOCATOR_BREAD_TAB).click()
        assert driver.find_element(*Locators.LOCATOR_CHOSEN_TAB).text == 'Булки', \
            'Переход из раздела "Начинки" в "Булки" в конструкторе'
