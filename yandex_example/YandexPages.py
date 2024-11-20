from BaseAppExample import BasePage
from selenium.webdriver.common.by import By


class YandexSeacrhLocators:
    # описываем локаторы
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")  # локатор поисковой строки
    LOCATOR_YANDEX_SEARCH_BUTTON = (
        By.CLASS_NAME, "search3__button")  # локатор кнопки “Найти”
    # локатор бара навигации (Картинки, Видео и т.д.)
    LOCATOR_YANDEX_NAVIGATION_BAR = (
        By.CSS_SELECTOR, "div.HeaderNav-DynamicTabs")


class SearchHelper(BasePage):
    # вспомогательные методы для работы с поиском
    def enter_word(self, word):
        search_field = self.find_element(
            YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(
            YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        elems = nav_bar_menu[0].split('\n')
        return elems
