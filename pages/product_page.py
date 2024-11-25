from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time


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
        print("ALERT_ABOUT_ADDED_BOOK: ", self.browser.find_element(
            *ProductPageLocators.ALERT_ABOUT_ADDED_BOOK).text)
        print("ALERT_BOOK_NAME: ", self.browser.find_element(
            *ProductPageLocators.ALERT_BOOK_NAME).text)
        print("BOOK_NAME: ", self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text)
        print("BOOK_PRICE: ", self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE).text)

    def should_be_alert_added_book_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_ABOUT_ADDED_BOOK), "Notification about added to the basket item is not present"

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
            *ProductPageLocators.ALERT_ABOUT_ADDED_BOOK).text.strip() == f"{book_name} has been added to your basket.", "Notification about added item is incorrect."

    def should_be_same_price(self, book_price):
        alert_book_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE).text.split(":")[-1].strip()
        assert alert_book_price == book_price, f'Added book price is incorrect. Added book price is "{alert_book_price}", but should be "{book_price}".'
