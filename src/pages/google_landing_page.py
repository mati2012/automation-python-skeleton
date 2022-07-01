from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.commons.base_page import BasePage
from src.commons.webdriversetup import locator_by
from src.pages.google_search_page import GoogleSearchPage


class GoogleLandingPage(BasePage):
    __INPUT_SEARCH = locator_by({
        'BY': By.CSS_SELECTOR,
        'LOCATOR': "[name='q']"
    })
    __SEARCH_BTN = locator_by({
        'BY': By.CSS_SELECTOR,
        'LOCATOR': "input[value='Buscar con Google']"
    })

    def __init__(self):
        super().__init__()

    def search_something(self, something_to_search: str):
        self.send_keys(self.__INPUT_SEARCH, something_to_search)
        self.get_element(self.__INPUT_SEARCH).send_keys(Keys.ENTER)
        return GoogleSearchPage()
