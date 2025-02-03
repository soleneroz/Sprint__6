import allure
import pytest
from conftest import driver
from pages.page_order import PageOrder
from locators.locators_main_page import LocatorsMainPage
from data import *


class TestOrderPage:

    @allure.title('Позитивный сценарий оформления заказа')
    @allure.description('Проверка оформления заказа из двух входных точек')
    @pytest.mark.parametrize('button, test_data', [(LocatorsMainPage.button_order_header, TestData.test_data_one), (LocatorsMainPage.button_order_main_page, TestData.test_data_two)])
    def test_order_all_fields_success(self, driver, button, test_data):
        page_order = PageOrder(driver)
        page_order.scroll_to_element(button)
        page_order.wait_element_is_visible(button)
        page_order.click_element(button)
        page_order.data_first_form(test_data)
        page_order.data_second_form(test_data)
        assert page_order.check_button_status_order_is_displayed()
