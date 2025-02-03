import allure
from locators.locators_order_page import LocatorsOrderPage
from pages.page_base import BasePage
from data import TestData


class PageOrder(BasePage):

    @allure.step('Клик на станцию метро')
    def select_subway_station(self):
        self.click_element(LocatorsOrderPage.select_item_in_multiselect)

    @allure.step('Выбор даты заказа')
    def send_keys_date(self):
        self.send_keys_input(LocatorsOrderPage.date).send_keys(TestData.test_data_one[5])

    @allure.step('Клик по дате заказа')
    def click_on_date_in_calendar(self):
        self.click_element(LocatorsOrderPage.calendar_item)

    @allure.step('Просмотр отображения кнопки статуса заказа')
    def check_button_status_order_is_displayed(self):
        return self.check_element_is_displayed(LocatorsOrderPage.button_check_status_order)

    @allure.step('Заполнение формы заказа, первая страница')
    def data_first_form(self, test_data):
        self.wait_element_is_visible(LocatorsOrderPage.name)
        self.click_element(LocatorsOrderPage.name)
        self.send_keys_input(LocatorsOrderPage.name, test_data[0])
        self.click_element(LocatorsOrderPage.surname)
        self.send_keys_input(LocatorsOrderPage.surname, test_data[1])
        self.click_element(LocatorsOrderPage.address)
        self.send_keys_input(LocatorsOrderPage.address, test_data[2])
        self.click_element(LocatorsOrderPage.subway_station)
        self.send_keys_input(LocatorsOrderPage.subway_station, test_data[3])
        self.click_element(LocatorsOrderPage.select_item_in_multiselect)
        self.click_element(LocatorsOrderPage.phone_number)
        self.send_keys_input(LocatorsOrderPage.phone_number, test_data[4])
        self.click_element(LocatorsOrderPage.button_next)

    @allure.step('Заполнение формы заказа, вторая страница')
    def data_second_form(self, test_data):
        self.wait_element_is_visible(LocatorsOrderPage.date)
        self.click_element(LocatorsOrderPage.date)
        self.send_keys_input(LocatorsOrderPage.date, test_data[5])
        self.click_element(LocatorsOrderPage.checkbox_grey_color_scooter)
        self.click_element(LocatorsOrderPage.checkbox_black_color_scooter)
        self.click_element(LocatorsOrderPage.field_rent_period)
        self.click_element(LocatorsOrderPage.multiselect_item_rent_period)
        self.click_element(LocatorsOrderPage.comment)
        self.send_keys_input(LocatorsOrderPage.comment, test_data[6])
        self.click_element(LocatorsOrderPage.button_make_order)
        self.wait_element_is_visible(LocatorsOrderPage.button_confirm_order)
        self.click_element(LocatorsOrderPage.button_confirm_order)
