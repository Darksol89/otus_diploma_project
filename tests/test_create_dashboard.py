import allure
import pytest
from PageObject.DashboardPage import DashboardPage
from PageObject.common.expected_results import ExpectedResults


@allure.title('Create dashboard')
@pytest.mark.parametrize('dash_name', ['OTUS'])
def test_create_dashboard(browser_driver, get_url, login_to_youtrack, dash_name):
    DashboardPage(browser_driver) \
        .click_dashboard_dropdown() \
        .create_new_dashboard(name=dash_name)

    assert dash_name == ExpectedResults(browser_driver).check_dashboard_name()

    DashboardPage(browser_driver) \
        .click_edit_dashboard() \
        .delete_dashboard(dash_name)
