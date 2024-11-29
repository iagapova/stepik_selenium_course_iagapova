from .base_page import BasePage
from .locators import BasePageLocators

# login_page.py - тут мы храним проверки авторизации и регистрации


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(
            *BasePageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(
            *BasePageLocators.REGISTER_FORM_PASSWORD1).send_keys(password)
        self.browser.find_element(
            *BasePageLocators.REGISTER_FORM_PASSWORD2).send_keys(password)
        self.browser.find_element(
            *BasePageLocators.REGISTRATION_SUBMIT).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert BasePageLocators.LOGIN_URL in self.browser.current_url, f"Login URL is not correct: {self.browser.current_url}"
        # assert "login" in browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *BasePageLocators.REGISTER_FORM), "Register form is not presented"
