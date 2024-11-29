from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# product_page.py - тут мы храним проверки связанные с товаром завернутые в класс ProductPage, который наследуется от класса BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        add_to_basket = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def print_text(self):
        print('----------------')
        print("BASKET_PRICE: ", self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE).text.split(":")[-1].strip())
        print("SUCCESS_ALERT_ADDED_BOOK: ", self.browser.find_element(
            *ProductPageLocators.SUCCESS_ALERT_ADDED_BOOK).text)
        print("ALERT_BOOK_NAME: ", self.browser.find_element(
            *ProductPageLocators.ALERT_BOOK_NAME).text)
        print("BOOK_NAME: ", self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text)
        print("BOOK_PRICE: ", self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE).text)

    def should_be_alert_added_book_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_ALERT_ADDED_BOOK), "Notification about added to the basket item is not present"

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def get_book_price(self):
        return self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE).text

    def should_be_same_book_name(self, book_name):
        alert_book_name = self.browser.find_element(
            *ProductPageLocators.ALERT_BOOK_NAME).text
        assert alert_book_name == book_name, f'Added book name is incorrect. Added book name is "{alert_book_name}", but should be "{book_name}".'

        assert self.browser.find_element(
            *ProductPageLocators.SUCCESS_ALERT_ADDED_BOOK).text.strip() == f"{book_name} has been added to your basket.", "Notification about added item is incorrect."

    def should_be_same_price(self, book_price):
        alert_book_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE).text.split(":")[-1].strip()
        assert alert_book_price == book_price, f'Added book price is incorrect. Added book price is "{alert_book_price}", but should be "{book_price}".'

    def should_not_be_success_message(self):
        # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT_ADDED_BOOK), \
            "Success message is presented, but should not be"

    def should_element_disappear(self):
        # будет ждать до тех пор, пока элемент не исчезнет
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT_ADDED_BOOK), \
            "Element is still presented, but should not be"
