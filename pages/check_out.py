from selenium.webdriver.common.by import By
from baseclass.baseclass import baseclass
from pages.search_product import SearchProduct

from utilities.utilis import Utils


class Checkout(SearchProduct):
    log = Utils.custom_logger()

    def __init__(self,driver):
        #super().__init__(driver)
        self.driver = driver

    # LOCATORS:
    cart_product_locator = "h4[class = 'media-heading']"
    checkout_button = "//button[@class ='btn btn-success']"

    # 1  Click_purchase_checkout_button
    def get_cart_product(self):
        checkout_product = self.driver.find_element(By.CSS_SELECTOR, "h4[class = 'media-heading']").text
        for item in self.selected_product:
            assert checkout_product in item, self.log.error("Assertion Fail")
            self.log.info("Assertion Pass")
    def click_purchase_checkout(self):
        self.get_cart_product()
        wait = baseclass(self.driver)
        wait.presence_of_element_located(By.XPATH, self.checkout_button ).click()
