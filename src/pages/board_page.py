import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.commons.base_page import BasePage
from src.commons.webdriversetup import locator_by


class BoardGame(BasePage):
    __ORANGE_TOKEN = locator_by({
        'BY': By.CSS_SELECTOR,
        'LOCATOR': "[name='space62']"
    })

    __ORANGE_TOKEN_SELECTED = locator_by({
        'BY': By.CSS_SELECTOR,
        'LOCATOR': '[src="you2.gif"]'
    })

    __SQUARE_1 = locator_by({
        'BY': By.CSS_SELECTOR,
        'LOCATOR': '[name="space53"]'
    })

    __SQUARE_2 = locator_by({
        'BY': By.CSS_SELECTOR,
        'LOCATOR': '[name="space44"]'
    })

    __BLUE_TOKEN_SELECTED = locator_by({
        'BY': By.CSS_SELECTOR,
        'LOCATOR': '[src="me2.gif"]'
    })

    __AGREE_BTN = locator_by({
        'BY': By.XPATH,
        'LOCATOR': "//*[text()='AGREE']"
    })

    def __init__(self):
        super().__init__()

    def accept_user_agrements(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.__AGREE_BTN))
        self.click_on_element(self.__AGREE_BTN)

    def move_token(self):
        self.click_on_element(self.__ORANGE_TOKEN)
        self.click_on_element(self.__SQUARE_1)
        time.sleep(3)
        self.click_on_element(self.__SQUARE_1)
        self.click_on_element(self.__SQUARE_2)
        time.sleep(2)

    def get_board_tokens(self):
        tokens = self.driver.find_elements(By.CSS_SELECTOR, '[src="you1.gif"]')
        return range(tokens)
