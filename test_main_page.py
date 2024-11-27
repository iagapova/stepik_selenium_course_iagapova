import pytest
from selenium import webdriver
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


# выполняем сами тесты
# Здесь мы будем создавать функции, которым:
# 1. выдаём нужный для проверки линк
# 2. создаем объект page класса MainPage
# 3. следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
# 4. добавляем проверки, которые создавали методами в main_page.py


def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    # реализация первого метода когда инициализация страницы находится в классе MainPage
    # login_page = page.go_to_login_page()
    # реализация второго метода когда инициализация страницы находитя в тесте
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_info_basket_content()
    page.should_be_empty_basket()
    page.should_not_be_success_message()


if __name__ == "__main__":
    print("НАЧАЛО")
    pytest.main()

# pytest -v --tb=line --language=en test_main_page.py
