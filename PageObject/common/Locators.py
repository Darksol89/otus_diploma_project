"""Different locators for elements in web application"""
from selenium.webdriver.common.by import By

class Login:
    """Locators for Login page without authorization"""
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[data-test='username-field']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[data-test='password-field']")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, ".form-row button[data-test='login-button']")
    LOG_IN_AS_GUEST = (By.CSS_SELECTOR, ".login-page__bottom-panel a[data-test='login-as-guest-button']")

class Dashboard:
    """Locators for Dashboard page"""
    YT_LOGO = (By.CSS_SELECTOR, "#headerContainer a[data-test='ring-link']")
    CONTEXT_SEARCH_DROPDOWN = (By.CSS_SELECTOR, ".yt-search-panel__context button")
    QUERY_FIELD = (By.CSS_SELECTOR, "div[data-test='ring-query-assist-input']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div .yt-search-panel__apply__button")
    ADD_TO_FAVORITES_DASHBOARD = (By.CSS_SELECTOR, "button[data-test='dashboard-add-to-favorites']")
    ADD_WIDGET = (By.CSS_SELECTOR, "button[data-test='add-widget-button']")
    GET_MORE_WIDGETS = (By.CSS_SELECTOR, "[data-test='ring-select-toolbar'] a")
    EDIT_BUTTON = (By.CSS_SELECTOR, "button[data-test='edit-dashboard-dropdown']")
    RENAME_OPTION = (By.CSS_SELECTOR, "span[title='Rename']")
    DASHBOARD_DROPDOWN = (By.CSS_SELECTOR, "span[data-test='dashboards-dropdown']")

class NavigationMenu:
    """Locators for Navigation Menu"""
    NEW_ISSUE_BUTTON = (By.CSS_SELECTOR, "button[data-test='createIssueButton']")
    ISSUES = (By.CSS_SELECTOR, "a[ng-href='issues']")
    ISSUES_DROPDOWN = (By.CSS_SELECTOR, "span[data-test='savedSearchAnchor']")
    DASHBOARDS = (By.CSS_SELECTOR, "a[data-test-id='Dashboard']")
    AGILE_BOARDS = (By.CSS_SELECTOR, "a[data-test-id='Agile Boards']")
    REPORTS = (By.CSS_SELECTOR, "a[data-test-id='Reports']")
    PROJECTS = (By.CSS_SELECTOR, "a[data-test-id='Projects']")
    KNOWLEDGE_BASE = (By.CSS_SELECTOR, "a[data-test-id='Knowledge Base']")

class HeaderTray:
    """Locators for Header Tray area"""
    NOTIFICATIONS = (By.CSS_SELECTOR, "div[data-test='ring-dropdown header-notifications']")
    ADMINISTRATION = (By.CSS_SELECTOR, "div[data-test='ring-dropdown header-settings']")
    HELP = (By.CSS_SELECTOR, "div[data-test='ring-dropdown header-help']")
    PROFILE = (By.CSS_SELECTOR, "div[data-test='ring-dropdown ring-profile']")
    LOG_IN = (By.CSS_SELECTOR, "button[data-test='ring-header-login-button']")
