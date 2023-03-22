import pytest
from selenium.webdriver.support.wait import WebDriverWait
from pages.purchase import PurchaseProduct
from ddt import ddt, data, unpack, file_data
import unittest
from utilities.utilis import Utils


@pytest.mark.usefixtures('setup')
@ddt
class TestPurchaseItem(unittest.TestCase):  # unittest.TestCase: is used to run DDT or else throws error

# 1 - Using DDT method
  #   @data(("Nokia Edge", 'India'), ("Samsung Note 8", 'India'))
# 2 - Using DDT with Json file
  #   @file_data(r"testdata\testdata_json.json")
# 3 - Using DDT with Excel file
  #   # Here "*" is used to unpack list data, if its tuple, then no need to use "*"
  #   @data(*Utils.read_excel_data(r"testdata\excel_data.xlsx", "Sheet1"))

# 4 - Using DDT with CSV file
    @data(*Utils.read_csv_data(r"testdata\testdata_csv.csv"))
    @unpack
    def test_purchase_phone(self,phone_name, country ):
        wait = WebDriverWait(self.driver,10)
        #Page-1
        purchase_product = PurchaseProduct(self.driver)
        #purchase_product.add_product("Nokia Edge")     # Without DDT method
        purchase_product.add_product(phone_name)           # Using DDT method
        purchase_product.clickOn_checkout()
        # Page-2
        purchase_product.click_purchase_checkout()
        # Page-3
        #purchase_product.select_country("India")       # Without DDT method
        purchase_product.select_country(country)        # Using DDT method
        purchase_product.clickOn_terms_conditions()
        purchase_product.clickOn_purchase()
        purchase_product.display_success_message()
        #Clear Data
        purchase_product.clear_data()


