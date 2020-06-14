import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from PageObject.LoginPage import LoginPage


def pytest_addoption(parser):
    """Parameters for running from command-line"""
    parser.addoption('--url',
                     action='store',
                     default='http://localhost:8080',
                     help='Url for YouTrack dashboard')
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help='Web browser for starting tests: Chrome or Firefox')
    parser.addoption('--username',
                     action='store',
                     default='admin',
                     help='Username for authorizing')
    parser.addoption('--password',
                     action='store',
                     default='admin',
                     help='Password for authorizing')


@pytest.fixture()
def browser_driver(request):
    """Initializing webdriver and start web browser"""
    browser = request.config.getoption('--browser_name')
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    yield browser
    browser.quit()


@pytest.fixture()
def get_url(request, browser_driver):
    """Open url for testing"""
    url = request.config.getoption('--url')
    open_link = browser_driver.get(url)
    browser_driver.implicitly_wait(7)

    return open_link

@pytest.fixture()
def login_to_youtrack(request, browser_driver):
    """Input username and password for authorization"""
    username = request.config.getoption('--username')
    password = request.config.getoption('--password')
    LoginPage(browser_driver) \
        .open_login_page() \
        .login_as_user(username=username, password=password)
