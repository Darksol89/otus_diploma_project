"""Special methods for working with Dashboard page"""

from PageObject.BasePage import BasePage
from PageObject.common.Locators import Dashboard, Alerts


class DashboardPage(BasePage):

    def click_edit_dashboard(self):
        """Click Edit dashboard button"""
        self._click_to_element(Dashboard.EDIT_BUTTON)
        return self

    def rename_dashboard(self, name):
        """Rename dashboard"""
        self._click_to_element(Dashboard.RENAME_OPTION)
        self.driver.find_element(*Dashboard.NAME_FIELD).clear()
        self._send_keys(name, Dashboard.NAME_FIELD)
        self._click_to_element(Dashboard.SAVE_BUTTON)
        return self

    def delete_dashboard(self, name):
        """Delete dashboard"""
        self._click_to_element(Dashboard.DELETE_OPTION)
        self._wait_element_text(Alerts.ALERT_MESSAGE, text=name)
        return self

    def click_dashboard_dropdown(self):
        """Open dashboard dropdown menu"""
        self._click_to_element(Dashboard.DASHBOARD_DROPDOWN)
        return self

    def create_new_dashboard(self, name):
        """Create new dashboard"""
        self._click_to_element(Dashboard.NEW_DASHBOARD)
        self._send_keys(name, Dashboard.NAME_FIELD)
        self._click_to_element(Dashboard.CREATE_BUTTON)
        self._wait_element_text(Dashboard.DASHBOARD_DROPDOWN, text=name)
        return self

    def click_add_widget(self):
        """Open widget dropdown list"""
        self._click_to_element(Dashboard.ADD_WIDGET)
        return self

    def click_add_widget_wiki_notes(self):
        """Open Wiki Notes widget dialog"""
        self._click_to_element(Dashboard.ADD_WIKI_NOTES)
        return self
