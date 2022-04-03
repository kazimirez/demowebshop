import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--is_headless', action='store', default='false',
                     help="need headless or not?")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    is_headless = request.config.getoption("is_headless")
    if browser_name == "chrome":
        if is_headless == 'true':
            options = Options()
            options.headless = True
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome(options=options)
        elif is_headless == 'false':
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome()
        else:
            raise pytest.UsageError("-- choose if true or false for headless mode")

    elif browser_name == "firefox":
        if is_headless == 'true':
            print("\nstart firefox browser for test..")
            options = FirefoxOptions()
            options.add_argument("--headless")
            browser = webdriver.Firefox(options=options)
        elif is_headless == 'false':
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox()
        else:
            raise pytest.UsageError("-- choose if true or false for headless mode")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()
