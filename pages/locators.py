from selenium.webdriver.common.by import By

# locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


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
    BASKET_CONTENT_MESSAGE = (
        By.CSS_SELECTOR, ".content p")
    BASKET_ITEMS = (
        By.CSS_SELECTOR, ".basket-items")
