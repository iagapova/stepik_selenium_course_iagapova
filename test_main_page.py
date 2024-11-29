import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


# выполняем сами тесты
# Здесь мы будем создавать функции, которым:
# 1. выдаём нужный для проверки линк
# 2. создаем объект page класса MainPage
# 3. следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
# 4. добавляем проверки, которые создавали методами в main_page.py

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    # проверка наличия сообщения о пустой корзине
    basket_page.should_be_info_basket_content()
    basket_page.is_basket_empty()  # проверка правильности сообщения о пустой корзине
    # проверяем что нет продуктов в корзине
    basket_page.should_not_be_basket_items()


if __name__ == "__main__":
    print("НАЧАЛО")
    pytest.main()

# pytest -v --tb=line --language=en test_main_page.py
# pytest -v -s -m login_guest --tb=line --language=en test_main_page.py
