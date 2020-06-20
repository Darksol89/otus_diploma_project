"""Special methods for working with Issue page"""

from PageObject.BasePage import BasePage
from PageObject.common.Locators import Issue


class IssuePage(BasePage):

    def add_summary_issue(self, issue_name):
        self._send_keys(issue_name, Issue.ISSUE_SUMMARY)
        return self

    def add_description_issue(self, description):
        self._send_keys(description, Issue.ISSUE_DESCRIPTION)
        return self

    def click_create_button(self):
        self._click_to_element(Issue.CREATE_ISSUE_BTN)
        return self

    def click_cancel_button(self):
        self._click_to_element(Issue.CANCEL_BTN)
        return self
