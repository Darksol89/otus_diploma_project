import allure
from PageObject.NavigationMenuPage import NavigationMenuPage
from PageObject.common.Locators import AgileBoards


@allure.title('Open Agile Board')
def test_open_agile_board_page(browser_driver, get_url, login_to_youtrack):
    """Test - open agile board page"""
    NavigationMenuPage(browser_driver).click_agile_board()

    assert browser_driver.find_element(*AgileBoards.CREATE_SCRUM_BOARD)
