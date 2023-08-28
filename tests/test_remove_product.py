import unittest
from selenium.webdriver import Firefox
from pages.product_page import ProductPage
import  time

class ProcedimentoTesteProduto(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.product_page = ProductPage(self.driver)

    def test_remove_from_cart(self):
        self.product_page.add_product_to_cart()

        time.sleep(3) #isso aqui é só pra dar tempo de visualmente verificar que saiu do carrinho
        
        self.product_page.remove_from_cart()

        cart_icon_text = self.product_page.get_cart_icon_text()
        self.assertEqual(cart_icon_text, '')  
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()