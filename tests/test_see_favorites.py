import unittest
from selenium.webdriver import Firefox
from pages.login_page import LoginPage
import time

class ProcedimentoTesteFavoritos(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = Firefox()
        self.login_page = LoginPage(self.driver)

    def test_open_favorites_page(self):
                
        # Realize o login usando os métodos da página de login
        self.login_page.fill_credentials('madyfabricio@gmail.com', 'Teste1234')
        self.login_page.perform_login()
        
        time.sleep(3)

        self.login_page.get_favorites()

        # Verifique se o redirecionamento para a página de favoritos ocorreu
        self.assertIn(self.driver.current_url,'https://www.kabum.com.br/minha-conta/favoritos')

    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()