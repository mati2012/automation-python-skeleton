class TestBoardGame():

    def test_livecoding1(self, open_boardgame):
        boardgame_page = open_boardgame
        boardgame_page.accept_user_agrements()
        boardgame_page.move_token()
        assert boardgame_page.get_board_tokens() < 12
