from YandexPages import SearchHelper


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Hello")
    yandex_main_page.click_on_the_search_button()
    elements = yandex_main_page.check_navigation_bar()
    assert "картинки" and "видео" in elements

# pytest -v --tb=line yandex_example/test_example_yandex.py
