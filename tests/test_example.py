import pytest
import time

@pytest.mark.parametrize(
    'test_word', ['Google', 'Yandex']
)
def test_google_title(browser, test_word):
    browser.get("http://www.google.com")
    # driver.maximize_window()
    time.sleep(2)
    assert test_word in browser.title


# pytest -v --browser=firefox  tests\test_example.py
