import allure
import pytest
from PageObject.DashboardPage import DashboardPage
from PageObject.NavigationMenuPage import NavigationMenuPage
from PageObject.IssuePage import IssuePage
from PageObject.common.expected_results import ExpectedResults


@allure.title('Add new issue testing')
@pytest.mark.parametrize('dash_name, issue_name', [('Space', 'Space_issue')])
def test_add_new_issue(browser_driver, get_url, login_to_youtrack, dash_name, issue_name):
    DashboardPage(browser_driver) \
        .click_dashboard_dropdown() \
        .create_new_dashboard(dash_name)
    NavigationMenuPage(browser_driver).click_new_issue()
    IssuePage(browser_driver) \
        .add_summary_issue(issue_name) \
        .add_description_issue(issue_name) \
        .click_create_button()

    assert issue_name == ExpectedResults(browser_driver).check_issue_name()

    NavigationMenuPage(browser_driver).click_dashboards()
    DashboardPage(browser_driver) \
        .click_edit_dashboard() \
        .delete_dashboard(dash_name)
