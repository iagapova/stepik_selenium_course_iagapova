import pytest
from selenium import webdriver
from .pages.locators import BasePageLocators
# from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time

# links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#          pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                       marks=pytest.mark.xfail(reason='Bug in this promo-link')),
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

# links = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]

# @pytest.mark.parametrize("link", links)
# def test_guest_can_add_book_to_basket(browser, link):


@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Bug in this promo-link')) for i in range(10)])
def test_guest_can_add_book_to_basket(browser, promo_offer):

    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()  # добавляем товар в корзину
    time.sleep(1)
    page.solve_quiz_and_get_code()  # вычисляем выражение и записываем его в алерт
    time.sleep(1)
    # page.print_text()  # печатаем переменные
    # проверка нотификации о том что продукт добавлен
    page.should_be_alert_added_book_to_basket()
    # проверка корректности имени книги
    page.should_be_same_book_name(page.get_book_name())
    # проверка корректности цены книги
    page.should_be_same_price(page.get_book_price())


def test_guest_can_add_book_to_basket_check_methods(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    # проверяем что ообщение об успешном добавлении книги в корзину не появляется в течении 4 секунд
    page.should_not_be_success_message()
    # проверяем что сообщение об успешном добавлении книги в корзину пропадает через 4 секунды
    page.should_element_disappear()
    page.add_product_to_basket()  # добавляем товар в корзину
    time.sleep(1)
    page.solve_quiz_and_get_code_old()  # вычисляем выражение и записываем его в алерт
    time.sleep(1)
    # page.print_text()  # печатаем переменные
    # проверка нотификации о том что продукт добавлен
    page.should_be_alert_added_book_to_basket()
    # проверка корректности имени книги
    page.should_be_same_book_name(page.get_book_name())
    # проверка корректности цены книги
    page.should_be_same_price(page.get_book_price())


@pytest.mark.xfail(reason="for test work of the method - not an issue")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()  # добавляем товар в корзину
    time.sleep(1)
    page.solve_quiz_and_get_code()  # вычисляем выражение и записываем его в алерт
    time.sleep(1)
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="for test work of the method - not an issue")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()  # добавляем товар в корзину
    time.sleep(1)
    page.solve_quiz_and_get_code()  # вычисляем выражение и записываем его в алерт
    time.sleep(1)
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_element_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    # реализация первого метода когда инициализация страницы находится в классе BasePage
    # login_page = page.go_to_login_page()
    # реализация второго метода когда инициализация страницы находитя в тесте
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


if __name__ == "__main__":
    print("НАЧАЛО")
    pytest.main()

# pytest -v -s --tb=line --language=en test_product_page.py
# pytest --headless=true -v -s --tb=line --language=en test_product_page.py
# pytest --headless=true -v -rx --tb=short --language=en test_product_page.py
