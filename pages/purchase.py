from selenium.webdriver.common.by import By
from baseclass.baseclass import baseclass
from pages.check_out import Checkout
from utilities.utilis import Utils


class PurchaseProduct(Checkout):
    log = Utils.custom_logger()

    def __init__(self,driver):
        #super().__init__(driver)
        self.driver = driver

    # LOCATORS:
    search_country_locator = "country"
    search_results_locator = "//div[@class = 'suggestions']"
    terms_conditions_locator = "//label[@for = 'checkbox2']"
    purchase_button_locator = "//input[@class ='btn btn-success btn-lg']"
    sucess_message_locator = "//div[@class ='alert alert-success alert-dismissible']"

    #1 Select_country
    def get_country_locatori(self, country_name):
        self.driver.find_element(By.ID, self.search_country_locator).send_keys(country_name)
        countries = self.driver.find_elements(By.XPATH, self.search_results_locator)
        for country in countries:
            if country.text == country_name:
                country.click()
    def select_country(self,enter_country_name):
        self.get_country_locatori(country_name = enter_country_name)

    #2 Select_terms_conditions
    def get_terms_conditions_locator(self):
        return self.driver.find_element(By.XPATH, self.terms_conditions_locator)
    def clickOn_terms_conditions(self):
        self.get_terms_conditions_locator().click()

    #3 Click_purchase_button
    def get_purchase_button(self):
        return self.driver.find_element(By.XPATH, self.purchase_button_locator)
    def clickOn_purchase(self):
        self.get_purchase_button().click()

     #4 Display_Message
    def get_success_locator(self):
        return self.driver.find_element(By.XPATH,self.sucess_message_locator ).text
    def display_success_message(self):
        self.log.info(self.get_success_locator())

    #5  Clear Data
    def clear_data(self):
        Checkout.selected_product.clear()
        assert len(Checkout.selected_product) is 0, self.log.warnning("Data not empty")
        self.log.info("Data cleared")

