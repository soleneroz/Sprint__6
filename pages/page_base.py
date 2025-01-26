from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.locators_main_page import LocatorsMainPage


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидаение загрузки элемента')
    def wait_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Клик на элемент')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввод значения в поле')
    def send_keys_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получение текста элемента')
    def get_text_at_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Переход на другую вкладку')
    def switch_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверка отображения элемента после загрузки')
    def check_element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Проверка заголовка страницы')
    def get_page_title(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(LocatorsMainPage.title_page))
        return self.driver.title
