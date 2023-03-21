from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class baseclass():

    def __init__(self,driver):
        self.driver = driver


    def presence_of_element_located(self,locator_type, locator):
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(expected_conditions.presence_of_element_located(
            (locator_type, locator)))


    def element_to_be_clickable(self, locator_type, locator):
        self.wait = WebDriverWait(self.driver, 10)
        return self.wait.until(expected_conditions.element_to_be_clickable(
            (locator_type, locator)))