import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

#  conftest.py - тут находится фикстура инициализации браузера, его запуск и закрытие, а также передача параметров  командной строке


def pytest_addoption(parser):  # обработчик опции
    parser.addoption('--browser_name',
                     action='store',
                     default="chrome",  # default="chrome"
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default="en",
                     help="Choose language: '--language=en' or '--language=ru'")
    parser.addoption('--headless',  # параметр для запуска тестов в фоновом режиме
                     action='store',
                     default="false",  # default значение
                     help="Run in headless mode: 'true' or 'false'")


@pytest.fixture(scope="function")  # обрабатывает переданные в опции данные
def browser(request):
    browser_name = request.config.getoption(
        "browser_name")  # логика обработки командной строки
    headless = request.config.getoption('headless').lower() == 'true'
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    if headless:
        # добавляем только если headless=true
        options.add_argument('--headless')

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)
    if headless:
        options_firefox.add_argument('--headless')

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

    # pytest -v --tb=line --reruns 1 --browser_name=chrome --language=ru 3/test_rerun.py
    # pytest -v --tb=line --reruns 1 --browser_name=chrome --language=en 3/test_rerun.py
