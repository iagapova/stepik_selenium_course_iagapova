from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time


class BasketPage(BasePage):

    def print_text(self):
        print('----------------')
        print("SUCCESS_ALERT_ADDED_BOOK: ", self.browser.find_element(
            *BasketPageLocators.BASKET_INFO_MESSAGE).text)

    def should_be_info_basket_content(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_INFO_MESSAGE), "Notification with basket info is not present"

    def should_be_empty_basket(self):
        basket_content_info = self.browser.find_element(
            *BasketPageLocators.BASKET_INFO_MESSAGE).text.split(". ")[0].strip()
        assert basket_content_info == "Your basket is empty", f'Basket info message is "{basket_content_info}", but should be "Your basket is empty".'

    def should_not_be_success_message(self):
        # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT_ADDED_BOOK), \
            "Success message is presented, but should not be"
