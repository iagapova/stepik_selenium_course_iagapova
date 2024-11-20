import time
from selenium import webdriver
# - класс, который содержит все возможные локаторы
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("https://ya.ru/")
    time.sleep(30)
    browser.find_element(By.ID, "text").send_keys("Hello!")
    browser.find_element(By.CLASS_NAME, "search3__button").click()
    all_elements = browser.find_elements(
        By.CSS_SELECTOR, "div.HeaderNav-DynamicTabs")
    print(all_elements)
    print('=============')
    # nav_bar_menu = []
    # for x in all_elements:
    #     print('----', x, x.text)
    #     print('++++', nav_bar_menu)
    #     if len(x.text) > 0:
    #         nav_bar_menu.append(x.text)
    nav_bar_menu = [x.text for x in all_elements if len(x.text) > 0]
    elems = nav_bar_menu[0].split('\n')
    print("elems= ", elems)
    time.sleep(5)
finally:
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    browser.quit()
