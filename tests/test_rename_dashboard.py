import allure
import pytest
from PageObject.DashboardPage import DashboardPage
from PageObject.common.expected_results import ExpectedResults

@allure.title('Rename dashboard testing')
@pytest.mark.parametrize('Name_1, Name_2', [('Jaguar', 'Eagle')])
def test_rename_dashboard(browser_driver, get_url, login_to_youtrack, Name_1, Name_2):
    """Test for rename created dashboard"""
    DashboardPage(browser_driver) \
        .click_dashboard_dropdown() \
        .create_new_dashboard(name=Name_1)\
        .click_edit_dashboard()\
        .rename_dashboard(name=Name_2)

    assert Name_2 == ExpectedResults(browser_driver).check_dashboard_name()

    DashboardPage(browser_driver) \
        .click_edit_dashboard() \
        .delete_dashboard(Name_2)