from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

# main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице.
# Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py


class MainPage(BasePage):
    def go_to_login_page(self):
        # символ * указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # проинициализируем новый объект Page и вернем его
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # обработка alert
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK), "Login link is not presented"
