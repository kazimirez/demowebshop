import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}


def pytest_collection_modifyitems(items, config):
    for item in items:
        if not any(item.iter_markers()):
            item.add_marker("unmarked")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--browser_language', action='store', default='en',
                     help="language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("browser_language")

    if browser_name in supported_browsers:
        browser = supported_browsers.get(browser_name, browser_language)()
        print(f"\nstart {browser_name} browser for test..")
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(
            f"--browser_name is invalid, supported browsers: {joined_browsers}")
    browser.implicitly_wait(1)
    yield browser
    print("\nquit browser..")
    browser.quit()
