from selenium.webdriver.common.by import By
from baseclass.baseclass import baseclass
from utilities.utilis import Utils


class SearchProduct():
    log = Utils.custom_logger()
    selected_product = []

    def __init__(self,driver):
        #super().__init__(driver)
        self.driver = driver

    # LOCATORS:
        # search_add_product
    search_product_locator = "[class='card h-100']"
    search_product_name_locator = "div/h4"
    add_product_buton = "div/button"
        # Checkout_menu
    checkout_menu_locator = "//span[@class = 'navbar-toggler-icon']"
    checkout_buton_locator = "//a[@class ='nav-link btn btn-primary']"


    # 1  Selecting_Product
    def get_search_product_locator(self, product_name):
        products = self.driver.find_elements(By.CSS_SELECTOR, self.search_product_locator)
        for product in products:
            if product.find_element(By.XPATH, self.search_product_name_locator).text == product_name:
                product.find_element(By.XPATH, self.add_product_buton).click()
                self.selected_product.append(product.find_element(By.XPATH,self.search_product_name_locator).text)
                self.log.info(self.selected_product)
    def add_product(self,enter_product_name):
        self.get_search_product_locator(product_name=enter_product_name)

    # 2  click_checkout_button
    def clickOn_checkout(self):
        wait = baseclass(self.driver)
        # ----***   following command is only applicable when browser window is not 'maximize'  ***----
        #wait.presence_of_element_located(By.XPATH,self.checkout_menu_locator).click()
        wait.element_to_be_clickable(By.XPATH,self.checkout_buton_locator).click()
