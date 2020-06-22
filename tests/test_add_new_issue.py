import allure
import pytest
from PageObject.NavigationMenuPage import NavigationMenuPage
from PageObject.IssuePage import IssuePage
from PageObject.common.expected_results import ExpectedResults


@allure.title('Add new issue testing')
@pytest.mark.parametrize('issue_name', [('Space-X_issue')])
def test_add_new_issue(browser_driver, get_url, login_to_youtrack, issue_name):
    """Test - Create new issue"""
    NavigationMenuPage(browser_driver).click_new_issue()
    IssuePage(browser_driver) \
        .add_summary_issue(issue_name) \
        .add_description_issue(issue_name) \
        .click_create_button()

    assert issue_name == ExpectedResults(browser_driver).check_issue_name()
