"""Methods for working with Agile Boards"""

from PageObject.BasePage import BasePage
from PageObject.common.Locators import AgileBoards


class AgileBoardPage(BasePage):

    def check_existing_board(self):
        try:
            self.driver.find_element(*AgileBoards.SETTINGS_BTN)
            self.click_settings_button()\
                .click_delete_board_button()\
                .click_confirm_ok_button()
        except:
            pass
        return self

    def click_create_scrum_board(self):
        self._click_to_element(AgileBoards.CREATE_SCRUM_BOARD)
        self._wait_for_loading(AgileBoards.AGILE_NAME_FIELD)
        return self

    def click_create_kanban_board(self):
        self._click_to_element(AgileBoards.CREATE_KANBAN_BOARD)
        self._wait_for_loading(AgileBoards.AGILE_NAME_FIELD)
        return self

    def input_agile_name(self, text):
        self._send_keys(text, AgileBoards.AGILE_NAME_FIELD)
        return self

    def add_project(self):
        self._click_to_element(AgileBoards.ADD_ALL_PROJECTS_LINK)
        return self

    def click_create_button(self):
        self._click_to_element(AgileBoards.CREATE_BOARD_BTN)
        #self._wait_for_loading(AgileBoards.SETTINGS_BTN)
        return self

    def click_settings_button(self):
        self._click_to_element(AgileBoards.SETTINGS_BTN)
        self._wait_for_loading(AgileBoards.CLONE_BOARD_BTN)
        return self

    def click_delete_board_button(self):
        self._click_to_element(AgileBoards.DELETE_BOARD_BTN)
        self._wait_for_loading(AgileBoards.CONFIRM_OK_BTN)
        return self

    def click_confirm_ok_button(self):
        self._click_to_element(AgileBoards.CONFIRM_OK_BTN)
        self._wait_for_loading(AgileBoards.CREATE_SCRUM_BOARD)
        return self
