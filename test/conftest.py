import pytest

from src.pages.board_page import BoardGame


@pytest.fixture()
def open_boardgame(init_driver):
    boardgame_page = BoardGame()
    boardgame_page.navigate_to('https://www.gamesforthebrain.com/game/checkers/')
    return boardgame_page
