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
    SHARE_BUTTON = (By.CSS_SELECTOR, "button[data-test='share-dashboard-button']")
    RENAME_OPTION = (By.CSS_SELECTOR, "span[title='Rename']")
    DELETE_OPTION = (By.XPATH, "//span[contains(text(), 'Delete')]")
    DASHBOARD_DROPDOWN = (By.CSS_SELECTOR, "span[data-test='dashboards-dropdown']")
    NEW_DASHBOARD = (By.CSS_SELECTOR, "button[data-test='ring-select-toolbar-button']")
    NAME_FIELD = (By.CSS_SELECTOR, "input[data-test='dashboard-name-input']")
    SAVE_BUTTON = (By.XPATH, "//button[@data-test='dialog-footer-button']//ng-transclude[contains(text(), 'Save')]")
    CREATE_BUTTON = (By.XPATH, "//button[@data-test='dialog-footer-button']//ng-transclude[contains(text(), 'Create')]")
    CANCEL_BUTTON = (By.XPATH, "//button[@data-test='dialog-footer-button']//ng-transclude[contains(text(), 'Cancel')]")
    ADD_MARKDOWN_NOTES = (By.CSS_SELECTOR, "span[title='Markdown Notes']")
    ADD_WIKI_NOTES = (By.CSS_SELECTOR, "span[title='Wiki Notes']")


class Alerts:
    """Locators for Alert message"""
    ALERT_MESSAGE = (By.CSS_SELECTOR, "div[data-test='alert']")


class Widgets:
    """Locators for Widgets dialog windows"""
    WIDGET_TITLE = (By.CSS_SELECTOR, "input[data-test='widget-name-input']")
    SHOW_PREVIEW = (By.XPATH, "//span[contains(text(), 'Show preview')]")
    CREATE_WIDGET_BTN = (By.CSS_SELECTOR, "button[data-test='widget-create']")
    CANCEL_WIDGET_BTN = (By.CSS_SELECTOR, "button[data-test='widget-cancel-creation']")
    REFRESH_FIELD = (By.CSS_SELECTOR, "input[data-test='widget-refresh-rate-input']")
    CREATE_NEW_REPORT = (By.CSS_SELECTOR, "//a[contains(text(), 'Create new report')]")
    SEARCH_REPORTS_FIELD = (By.CSS_SELECTOR, "input.youtrack-report__select-input")
    ISSUE_LIST_TITLE = (By.CSS_SELECTOR, "input.input_cc0")
    WIDGET_TITLE_FIELD = (By.CSS_SELECTOR, "input[data-test='widget-name-input']")
    WIKI_NOTES_TEXT_FIELD = (By.CSS_SELECTOR, "div[data-test='ring-island-content'] textarea")
    WIKI_NOTES_TEXT_RESULT = (By.CSS_SELECTOR, "div[data-test='wikiText']")
    WIDGET_DROPDOWN_MENU_BTN = (By.CSS_SELECTOR, "div[data-test='widget-actions-dropdown'] button")
    WIDGET_DROPDOWN_REMOVE = (By.XPATH, "//span[contains(text(), 'Remove')]")


class AgileBoards:
    """Locators for Agile boards"""
    CREATE_SCRUM_BOARD = (By.CSS_SELECTOR, "button[data-test='createScrumBoard']")
    CREATE_KANBAN_BOARD = (By.CSS_SELECTOR, "button[data-test='createKanbanBoard']")
    CREATE_VERSION_BOARD = (By.CSS_SELECTOR, "button[data-test='createVersionBoard']")
    CREATE_CUSTOM_BOARD = (By.CSS_SELECTOR, "button[data-test='createCustomBoard']")
    CREATE_PERSONAL_BOARD = (By.CSS_SELECTOR, "button[data-test='createPersonalBoard']")
    AGILE_NAME_FIELD = (By.CSS_SELECTOR, "input[name='name']")
    ADD_ALL_PROJECTS_LINK = (By.CSS_SELECTOR, "span[data-test='agileBoardAddTeamProjectsLink']")
    SPRINT_DROPDOWN_MENU = (By.CSS_SELECTOR, "button[select-instance='agileBoardCtrl.sprintSelect']")
    CREATE_BOARD_BTN = (By.CSS_SELECTOR, "button[data-test='saveNewBoard']")
    CANCEL_BOARD_BTN = (By.CSS_SELECTOR, "button[data-test='cancelNewBoardForm']")
    DELETE_BOARD_BTN = (By.XPATH, "//span[contains(text(), 'Delete board')]")
    CLONE_BOARD_BTN = (By.XPATH, "//span[contains(text(), 'Clone board')]")
    CONFIRM_OK_BTN = (By.CSS_SELECTOR, "button[data-test='confirm-ok-button']")
    CONFIRM_REJECT_BTN = (By.CSS_SELECTOR, "button[data-test='confirm-reject-button']")
    SETTINGS_BTN = (By.CSS_SELECTOR, "button[data-test='boardSettingsToggler']")


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


class Issue:
    """Locators for Issue page"""
    ISSUE_SUMMARY = (By.CSS_SELECTOR, "[data-test='issueSummary']")
    ISSUE_DESCRIPTION = (By.CSS_SELECTOR, "textarea[data-test='issueDescription']")
    OPEN_COMMAND_DIALOG_BTN = (By.CSS_SELECTOR, "button[title='Open command dialog']")
    LINK_ISSUE_BTN = (By.CSS_SELECTOR, "button[title='Link issue']")
    ADD_TAG_BTN = (By.CSS_SELECTOR, "button[title='Add tag']")
    ASSIGN_ISSUE_BTN = (By.CSS_SELECTOR, "button[title='Assign issue']")
    SHOW_MORE_BTN = (By.CSS_SELECTOR, "button[title='Show more']")
    CREATE_ISSUE_BTN = (By.CSS_SELECTOR, "button[data-test='createIssueAction']")
    CANCEL_BTN = (By.CSS_SELECTOR, "button[data-test='cancelAction']")
    ISSUE_SUMMARY_RESULT = (By.CSS_SELECTOR, "h1[data-test='issueSummary']")
