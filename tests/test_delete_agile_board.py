import pytest
import allure
from PageObject.NavigationMenuPage import NavigationMenuPage
from PageObject.AgileBoardPage import AgileBoardPage
from PageObject.common.Locators import AgileBoards


@allure.title('Create and delete board')
@pytest.mark.parametrize('agile_name', ['My Kanban board'])
def test_delete_agile_board(browser_driver, get_url, login_to_youtrack, agile_name):
    """Test - Create and Delete Kanban board"""
    NavigationMenuPage(browser_driver).click_agile_board()
    AgileBoardPage(browser_driver) \
        .check_existing_board() \
        .click_create_kanban_board() \
        .input_agile_name(agile_name) \
        .add_project() \
        .click_create_button() \
        .click_settings_button() \
        .click_delete_board_button() \
        .click_confirm_ok_button()

    assert browser_driver.find_element(*AgileBoards.CREATE_KANBAN_BOARD)
