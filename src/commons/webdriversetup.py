from selenium.webdriver.support.wait import WebDriverWait


def locator_by(selector):
    strategy = selector.get('BY')
    locator = selector.get('LOCATOR')
    return strategy, locator


class WebDriver:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=10)

    def get_element(self, locator: str):
        strategy, selector = locator
        return self.driver.find_element(strategy, selector)

    def send_keys(self, locator: str, string: str):
        element = self.get_element(locator)
        element.send_keys(string)

    def click_on_element(self, locator: str):
        element = self.get_element(locator)
        element.click()

    def is_element_visible(self, locator: str):
        element = self.get_element(locator)
        return element.is_displayed()

    def navigate_to(self, url: str):
        self.driver.get(url)
