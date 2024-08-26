from selenium.webdriver.common.by import By
import pytest
import time

link = "https://google.com"
link2 = "http://selenium1py.pythonanywhere.com/"



# @pytest.mark.skip
@pytest.mark.parametrize(
    'test_word', ['Google', 'Yandex']
)
def test_google_title(browser, test_word):
    browser.get(link)
    # driver.maximize_window()
    # time.sleep(2)
    assert test_word in browser.title


# Попробуем по локатору найти кнопку (сначала проверить в DevTools)
# Почему не переходит на английский по требованию??

# @pytest.mark.skip
def test_google_button(browser):
    browser.get(link)
    btn = browser.find_element(By.CSS_SELECTOR,".FPdoLc.lJ9FBc input.RNmpXc")
    time.sleep(5)
    assert btn.get_attribute("value") == "Мне повезёт!"
    # assert btn.get_attribute("value") == "I'm Feeling Lucky"


# @pytest.mark.skip
def test_google_button_transfer(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR,".FPdoLc.lJ9FBc input.RNmpXc").click()
    assert browser.current_url == "https://doodles.google/", 'URL changed to expected url'
    time.sleep(5)

    # assert btn.get_attribute("value") == "I'm Feeling Lucky"


# @pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    browser.get(link2)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
    time.sleep(4)




# pytest -v --browser=firefox  tests\test_example.py
# pytest -v  --language=en --browser=firefox  tests\test_example.py
# pytest --browser=firefox --language=es
# pytest --language=en
# pytest --browser=chrome --language=ru
# pytest --language=de
# pytest --language=fr