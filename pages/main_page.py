from .base_page import BasePage
from selenium.webdriver.common.by import By

# main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице.
# Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
