import pytest
from selenium import webdriver
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]


@pytest.mark.parametrize("link", links)
def test_guest_can_add_book_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # вычисляем выражение и записываем его в алерт
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
