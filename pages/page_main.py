import allure
from locators.locators_main_page import LocatorsMainPage
from pages.page_base import BasePage


class MainPage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Заказать" в хедере')
    def wait_button_order_in_header_is_visible(self):
        self.wait_element_is_visible(LocatorsMainPage.button_order_header)

    @allure.step('Клик по кнопке заказа в хедере')
    def click_button_order_in_header(self):
        self.click_element(LocatorsMainPage.button_order_header)

    @allure.step('Ожидание загрузки лого "Самокат"')
    def wait_scooter_logo_in_header_is_visible(self):
        self.wait_element_is_visible(LocatorsMainPage.header_scooter_logo)

    @allure.step('Ожидание загрузки лого "Яндекс"')
    def wait_yandex_logo_in_header_is_visible(self):
        self.wait_element_is_visible(LocatorsMainPage.header_yandex_logo)

    @allure.step('Клик по лого "Самокат"')
    def click_scooter_logo_in_header(self):
        self.click_element(LocatorsMainPage.header_scooter_logo)

    @allure.step('Клик по лого "Яндекс"')
    def click_yandex_logo_in_header(self):
        self.click_element(LocatorsMainPage.header_yandex_logo)

    @allure.step('Ожидание загрузки заголовка')
    def wait_header_is_visible(self):
        self.wait_element_is_visible(LocatorsMainPage.header)

    @allure.step('Проверка заголовка')
    def check_header_is_displayed(self):
        return self.check_element_is_displayed(LocatorsMainPage.header)

    @allure.step('Скролл до "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_element(LocatorsMainPage.faq)

    @allure.step('Ожидание загрузки в "Вопросы о важном"')
    def wait_faq_items_question_is_visible(self, data):
        self.wait_element_is_visible(LocatorsMainPage.faq_item_question[data])

    @allure.step('Клик на номер вопроса в "Вопросы о важном"')
    def click_faq_item(self, data):
        self.click_element(LocatorsMainPage.faq_item_question[data])

    @allure.step('Ожидание загрузки ответа в "Вопросы о важном"')
    def wait_faq_items_answers_is_visible(self, data):
        self.wait_element_is_visible(LocatorsMainPage.faq_item_answer[data])

    @allure.step('Текст ответа в "Вопросы о важном"')
    def get_text_answer_items_is_displayed(self, data):
        return self.get_text_at_element(LocatorsMainPage.faq_item_answer[data])
