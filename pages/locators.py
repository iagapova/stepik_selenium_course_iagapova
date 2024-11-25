from selenium.webdriver.common.by import By

# locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать


class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_PRICE = (
        By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"] strong')
    ALERT_ABOUT_ADDED_BOOK = (
        By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-success  fade in"] div')
    ALERT_BOOK_NAME = (
        By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-success  fade in"] div strong')
    BOOK_NAME = (
        By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (
        By.CSS_SELECTOR, 'p.price_color')
