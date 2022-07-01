import os
import pathlib

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_instance = None


def pytest_configure(config):
    os.environ["project_path"] = str(pathlib.Path(__file__).parent.absolute())


@pytest.fixture()
def init_driver():
    global driver_instance
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('ignore-certificate-errors')
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument('--headless')

    driver_instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    yield
    driver_instance.quit()


def get_driver_instance():
    global driver_instance
    if driver_instance is None:
        raise Exception("Can't get a driver instance. Reason: No driver instantiated.")
    return driver_instance
