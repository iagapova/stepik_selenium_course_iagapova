import pytest
from selenium import webdriver
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    # реализация первого метода когда инициализация страницы находится в классе MainPage
    # login_page = page.go_to_login_page()
    # реализация второго метода когда инициализация страницы находитя в тесте
    login_page = LoginPage(browser=browser, url=browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


if __name__ == "__main__":
    print("НАЧАЛО")
    pytest.main()

# pytest -v --tb=line --language=en test_main_page.py
