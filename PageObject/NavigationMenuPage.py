"""Special methods for working with Navigation Menu page"""

from PageObject.BasePage import BasePage
from PageObject.common.Locators import NavigationMenu



class NavigationMenuPage(BasePage):

    def click_new_issue(self):
        self._click_to_element(NavigationMenu.NEW_ISSUE_BUTTON)
        return self

    def click_agile_board(self):
        self._click_to_element(NavigationMenu.AGILE_BOARDS)
        return self

    def click_dashboards(self):
        self._click_to_element(NavigationMenu.DASHBOARDS)
        return self