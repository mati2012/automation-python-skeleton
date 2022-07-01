from conftest import get_driver_instance
from src.commons.webdriversetup import WebDriver


class BasePage(WebDriver):

    def __init__(self):
        super().__init__(get_driver_instance())


