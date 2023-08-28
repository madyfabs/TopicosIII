import unittest
from selenium.webdriver import Firefox
from pages.product_page import ProductPage

class ProcedimentoTesteItemCarrinho(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.product_page = ProductPage(self.driver)

    def test_add_to_cart(self):
        self.product_page.add_product_to_cart()

        success_message = self.product_page.get_success_message()
        self.assertIn('Produto adicionado com sucesso no carrinho', success_message)

        # Clique no ícone do carrinho
        self.product_page.go_to_cart()        

        self.product_page.get_item_from_cart()

        # Verifica se redirecionou para a página do carrinho
        self.assertEqual(self.driver.current_url, 'https://www.kabum.com.br/produto/401272/placa-de-video-rtx-3060-ti-1-click-oc-plus-galax-nvidia-geforce-8-gb-gddr6x-dlss-ray-tracing-36ism6md2kcv')
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()