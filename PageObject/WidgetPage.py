"""Methods for working with widgets"""

from PageObject.BasePage import BasePage
from PageObject.common.Locators import Widgets, Dashboard, Alerts
from PageObject.DashboardPage import DashboardPage
from selenium.webdriver.common.by import By

class WidgetPage(BasePage):

    def add_widget_title(self, widget_title):
        """Adding optional widget title"""
        self._send_keys(widget_title, Widgets.WIDGET_TITLE_FIELD)
        return self

    def add_widget_text(self, widget_text):
        """Adding widget text"""
        self._send_keys(widget_text, Widgets.WIKI_NOTES_TEXT_FIELD)
        return self

    def click_create_widget(self):
        """Click Create widget button"""
        self._click_to_element(Widgets.CREATE_WIDGET_BTN)
        return self

    def wait_widget(self, text):
        """Waiting created widget in dashboard"""
        self._wait_element_text(Widgets.WIKI_NOTES_TEXT_RESULT, text)
        return self

    def click_widget_dropdown_menu(self):
        """Click widget dropdown menu button"""
        self._click_to_element(Widgets.WIDGET_DROPDOWN_MENU_BTN)
        return self

    def click_widget_remove_option(self):
        """Select Remove option from dropdown menu"""
        self._click_to_element(Widgets.WIDGET_DROPDOWN_REMOVE)
        return self

    def wait_widget_remove_message(self, text):
        """Waiting alert message about remove widget"""
        self._wait_element_text(Alerts.ALERT_MESSAGE, text)
        return self

    def delete_wiki_notes_widget(self, widget_name=None):
        """Delete created widget Wiki Notes"""
        self._click_to_element(Widgets.WIDGET_DROPDOWN_MENU_BTN)
        self._click_to_element(Widgets.WIDGET_DROPDOWN_REMOVE)
        self._wait_element_text(Alerts.ALERT_MESSAGE, text=widget_name)
        return self
