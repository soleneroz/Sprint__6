import allure
from pages.page_main import MainPage
from conftest import driver
from data import TestData
import pytest


class TestFaq:

    @allure.title('"Вопросы о важном"')
    @allure.description('Проверка текста ответов')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_answer_faq)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        page_main = MainPage(driver)
        page_main.scroll_to_faq()
        page_main.wait_faq_items_question_is_visible(question_number)
        page_main.click_faq_item(question_number)
        page_main.wait_faq_items_answers_is_visible(question_number)
        assert page_main.get_text_answer_items_is_displayed(question_number) == expected_answer
