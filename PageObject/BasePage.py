"""Page Object pattern for Base Page"""

from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from PageObject.common.Locators import Dashboard


class BasePage:

    def __init__(self, driver):
        """Initialize web driver"""
        self.driver: WebDriver = driver

    def _click_to_element(self, locator):
        """Click to web element"""
        try:
            self.driver.implicitly_wait(3)
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(locator))
        except NoSuchElementException:
            print('Element is not found')
        finally:
            self.driver.find_element(*locator).click()

    def _send_keys(self, value, locator):
        """Send keys to specified locator"""
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def _selecting_by_visible_text(self, locator, text):
        """Selecting visible options from combo box"""
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text)

    def _wait_for_loading(self, locator):
        """Custom waitter web elements"""
        wait = WebDriverWait(self.driver, 5)
        try:
            self.driver.implicitly_wait(3)
            wait.until(ec.presence_of_element_located(locator))
        except NoSuchElementException:
            print('Element is not found')

    def _wait_element_text(self, locator, text):
        """Custom waitter for web elements text"""
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(ec.text_to_be_present_in_element(locator, text))
        except NoSuchElementException:
            print('Element is not found')

    def _wait_alert_popup(self):
        """Custom waitter for alert pop-up"""
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(ec.alert_is_present())
        except NoSuchElementException:
            print('Alert message in not found')