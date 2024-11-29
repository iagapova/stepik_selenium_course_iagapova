from .base_page import BasePage
from .locators import BasketPageLocators

# basket_page.py - тут мы храним проверки сообщений на странице корзины, завернутые в класс BasketPage, который наследуется от класса BasePage


class BasketPage(BasePage):
    def should_be_info_basket_content(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_CONTENT_MESSAGE), "Notification with basket info is not present"

    def is_basket_empty(self):
        expected_empty_basket_content_message = "Your basket is empty. Continue shopping"
        basket_content_message = self.browser.find_element(
            *BasketPageLocators.BASKET_CONTENT_MESSAGE).text
        assert basket_content_message == expected_empty_basket_content_message, f'Basket info message is "{basket_content_message}", but should be "{expected_empty_basket_content_message}".'

    def should_not_be_basket_items(self):
        # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Success message is presented, but should not be"
