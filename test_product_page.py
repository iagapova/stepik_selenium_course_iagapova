import pytest
from .pages.locators import BasePageLocators
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import time


# @pytest.mark.new
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # используем прямую ссылку логин страницы
        page = LoginPage(browser, BasePageLocators.LOGIN_URL)
        page.open()
        page.should_be_register_form()
        page.register_new_user(
            BasePage.generate_email(self), BasePage.generate_passw(self))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, browser.current_url)
        page.open()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()  # добавляем товар в корзину
        time.sleep(1)
        page.solve_quiz_and_get_code_old()  # вычисляем выражение и записываем его в алерт
        time.sleep(1)
        # проверка нотификации о том что продукт добавлен
        page.should_be_alert_added_book_to_basket()
        # проверка корректности имени книги
        page.should_be_same_book_name(page.get_book_name())
        # проверка корректности цены книги
        page.should_be_same_price(page.get_book_price())


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Bug in this promo-link')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):

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


def test_guest_can_add_product_to_basket_check_methods(browser):
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
    # проверка нотификации о том что продукт добавлен
    page.should_be_alert_added_book_to_basket()
    # проверка корректности имени книги
    page.should_be_same_book_name(page.get_book_name())
    # проверка корректности цены книги
    page.should_be_same_price(page.get_book_price())


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()  # переход в корзину
    # проверка наличия сообщения о пустой корзине
    page.should_be_info_basket_content()
    page.is_basket_empty()  # проверка правильности сообщения о пустой корзине
    page.should_not_be_basket_items()  # проверяем что нет продуктов в корзине


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


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


if __name__ == "__main__":
    print("НАЧАЛО")
    pytest.main()

# pytest -v -s --tb=line --language=en test_product_page.py
# pytest -v --tb=line --language=en -m need_review test_product_page.py

# @pytest.mark.new # для удобной маркировки и запуска свежих тестов
# pytest -v -s -m "new" --tb=line --language=en test_product_page.py

# для запуска тестов в фоновом режиме
# pytest --headless=true -v -s --tb=line --language=en test_product_page.py
# pytest --headless=true -v -rx --tb=short --language=en test_product_page.py
