import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


if __name__ == "__main__":
    print("НАЧАЛО")
    pytest.main()

# pytest -v --tb=line --language=en test_main_page.py
