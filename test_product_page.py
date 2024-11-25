import pytest
from selenium import webdriver
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                      marks=pytest.mark.xfail(reason='Bug in this promo-link')),
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

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


if __name__ == "__main__":
    print("НАЧАЛО")
    pytest.main()

# pytest -v -s --tb=line --language=en test_product_page.py
# pytest --headless=true -v -s --tb=line --language=en test_product_page.py
# pytest --headless=true -v -rx --tb=short --language=en test_product_page.py
