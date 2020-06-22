import allure
import pytest
from PageObject.DashboardPage import DashboardPage
from PageObject.WidgetPage import WidgetPage
from PageObject.NavigationMenuPage import NavigationMenuPage
from PageObject.common.expected_results import ExpectedResults


@allure.title('Adding widget in Dashboard')
@pytest.mark.parametrize('dash_name, widget_text', [('Fish', 'fish_widget_text')])
def test_add_widget_in_dashboard(browser_driver, get_url, login_to_youtrack, dash_name, widget_text):
    """Test - Adding  Wiki Notes widget"""
    DashboardPage(browser_driver) \
        .click_dashboard_dropdown() \
        .create_new_dashboard(dash_name) \
        .click_add_widget() \
        .click_add_widget_wiki_notes()
    WidgetPage(browser_driver) \
        .add_widget_text(widget_text) \
        .click_create_widget() \
        .wait_widget(widget_text)

    assert widget_text == ExpectedResults(browser_driver).check_widget_text()

    NavigationMenuPage(browser_driver).click_dashboards()
    DashboardPage(browser_driver) \
        .click_edit_dashboard() \
        .delete_dashboard(dash_name)
