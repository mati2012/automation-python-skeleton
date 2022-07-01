from selenium.webdriver.common.by import By

from src.commons.base_page import BasePage
from src.commons.webdriversetup import locator_by


class GoogleSearchPage(BasePage):
    __SEARCH_STATS = locator_by({
        'BY': By.ID,
        'LOCATOR': "result-stats"
    })

    def __init__(self):
        super().__init__()

    def is_result_stats_visible(self):
        return self.is_element_visible(self.__SEARCH_STATS)
