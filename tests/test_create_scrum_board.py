import pytest
import allure
from PageObject.NavigationMenuPage import NavigationMenuPage
from PageObject.AgileBoardPage import AgileBoardPage
from PageObject.common.Locators import AgileBoards

@allure.title('Create Scrum board testing')
@pytest.mark.parametrize('agile_name', ['The Best Scrum board'])
def test_create_scrum_board(browser_driver, get_url, login_to_youtrack, agile_name):
    NavigationMenuPage(browser_driver).click_agile_board()
    AgileBoardPage(browser_driver) \
        .check_existing_board() \
        .click_create_scrum_board() \
        .input_agile_name(agile_name) \
        .add_project() \
        .click_create_button()

    assert browser_driver.find_element(*AgileBoards.SPRINT_DROPDOWN_MENU)
