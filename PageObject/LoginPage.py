"""Special methods for Login page"""

from PageObject.BasePage import BasePage
from PageObject.common.Locators import Login, HeaderTray, Dashboard


class LoginPage(BasePage):

    def open_login_page(self):
        """Open page for authorization user"""
        self._click_to_element(HeaderTray.LOG_IN)
        return self

    def login_as_user(self, username, password):
        """Log In to site as User or Admin"""
        self._send_keys(username, Login.USERNAME_FIELD)
        self._send_keys(password, Login.PASSWORD_FIELD)
        self._click_to_element(Login.LOG_IN_BUTTON)
        self.wait_for_loading(Dashboard.YT_LOGO)
        return self

    def login_as_guest(self):
        """Log In to site as Guest"""
        self._click_to_element(Login.LOG_IN_AS_GUEST)
        self.wait_for_loading(Dashboard.YT_LOGO)
        return self