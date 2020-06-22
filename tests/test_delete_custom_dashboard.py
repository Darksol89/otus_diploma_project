import allure
import pytest
from PageObject.DashboardPage import DashboardPage
from PageObject.common.expected_results import ExpectedResults


@allure.title('Delete created dashboard')
@pytest.mark.parametrize('dash_name', ['Tiger'])
def test_delete_custom_dashboard(browser_driver, get_url, login_to_youtrack, dash_name):
    """Test - Delete created dashboard"""
    DashboardPage(browser_driver) \
        .click_dashboard_dropdown() \
        .create_new_dashboard(name=dash_name) \
        .click_edit_dashboard() \
        .delete_dashboard(name=dash_name)

    assert dash_name in ExpectedResults(browser_driver).check_alert_message()
