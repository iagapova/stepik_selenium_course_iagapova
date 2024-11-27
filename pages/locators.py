from selenium.webdriver.common.by import By

# locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_PRICE = (
        By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_ALERT_ADDED_BOOK = (
        By.CSS_SELECTOR, '.alert.alert-success div')
    ALERT_BOOK_NAME = (
        By.CSS_SELECTOR, '.alert.alert-success strong')
    BOOK_NAME = (
        By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (
        By.CSS_SELECTOR, 'p.price_color')


class BasketPageLocators():
    BASKET_INFO_MESSAGE = (
        By.CSS_SELECTOR, ".content p")
    BASKET_ITEMS = (
        By.CSS_SELECTOR, ".basket-items")
