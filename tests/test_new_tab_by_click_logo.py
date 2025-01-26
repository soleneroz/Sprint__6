import allure
from conftest import driver
from pages.page_main import MainPage


class TestLogo:

    @allure.title('Проверка открытия главной страницы "Самокат"')
    def test_logo_scooter_open_main_page(self, driver):
        page_main = MainPage(driver)
        page_main.wait_button_order_in_header_is_visible()
        page_main.click_button_order_in_header()
        page_main.wait_scooter_logo_in_header_is_visible()
        page_main.click_scooter_logo_in_header()
        page_main.wait_header_is_visible()
        assert page_main.check_header_is_displayed()

    @allure.title('Проверка открытия "Дзен"')
    def test_logo_yandex_open_dzen(self, driver):
        page_main = MainPage(driver)
        page_main.wait_yandex_logo_in_header_is_visible()
        page_main.click_yandex_logo_in_header()
        page_main.switch_next_tab()
        assert page_main.get_page_title() == 'Дзен — платформа для просмотра и создания контента. Вы всегда найдёте здесь то, что подходит именно вам: сотни тысяч авторов ежедневно делятся постами, статьями, видео и короткими роликами'
