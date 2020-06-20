"""Expected results for tests"""

from PageObject.BasePage import BasePage
from PageObject.common.Locators import Dashboard, Alerts, Issue, Widgets


class ExpectedResults(BasePage):

    def check_dashboard_name(self):
        custom_dash_name = self.driver.find_element(*Dashboard.DASHBOARD_DROPDOWN).text
        return custom_dash_name

    def check_alert_message(self):
        alert_pop_up = self.driver.find_element(*Alerts.ALERT_MESSAGE).text
        return alert_pop_up

    def check_issue_name(self):
        issue_summary = self.driver.find_element(*Issue.ISSUE_SUMMARY_RESULT).text
        return issue_summary

    def check_widget_text(self):
        """Check created widget from User"""
        widget_name = self.driver.find_element(*Widgets.WIKI_NOTES_TEXT_RESULT).text
        return widget_name
