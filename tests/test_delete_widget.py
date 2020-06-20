import allure
import pytest
from PageObject.DashboardPage import DashboardPage
from PageObject.WidgetPage import WidgetPage
from PageObject.common.expected_results import ExpectedResults

@allure.title('Delete widget testing')
@pytest.mark.parametrize('dash_name, widget_text', [('Shark', 'Shark_widget')])
def test_delete_widget(browser_driver, get_url, login_to_youtrack, dash_name, widget_text):
    """Test for delete widget"""
    DashboardPage(browser_driver) \
        .click_dashboard_dropdown() \
        .create_new_dashboard(dash_name) \
        .click_add_widget() \
        .click_add_widget_wiki_notes()
    WidgetPage(browser_driver) \
        .add_widget_text(widget_text) \
        .click_create_widget() \
        .wait_widget(widget_text)\
        .click_widget_dropdown_menu()\
        .click_widget_remove_option()\
        .wait_widget_remove_message(text='Wiki Notes')

    assert 'Wiki Notes' in ExpectedResults(browser_driver).check_alert_message()

    DashboardPage(browser_driver) \
        .click_edit_dashboard() \
        .delete_dashboard(dash_name)
