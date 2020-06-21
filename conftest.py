"""Special fixtures for tests working"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
        options.add_argument('headless')
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    elif browser == 'selenium-server-chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Remote(command_executor='http://host.docker.internal:4444/wd/hub',
                                   desired_capabilities=DesiredCapabilities.CHROME, options=options)
    elif browser == 'selenoid-chrome':
        capabilities = {
            "browserName": "chrome",
            "version": "83.0",
            "enableVNC": True,
            "enableVideo": False
        }
        browser = webdriver.Remote(
            command_executor="http://172.17.0.1:4445/wd/hub",
            desired_capabilities=capabilities)
        browser.maximize_window()

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


@pytest.fixture()
def login_as_guest_to_yt(browser_driver):
    """Log In to site as Guest"""
    LoginPage(browser_driver) \
        .open_login_page() \
        .login_as_guest()
