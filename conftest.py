from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption("--browser",
                     type=str,
                     help="my option:type1 or type2",
                     default="chrome")


# чтобы выбирать браузер в запросе, используем встроенную фикстуру request,
# и ей передаем значение browser_name
@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    yield browser
    browser.quit()
