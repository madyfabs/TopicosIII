import unittest
from selenium.webdriver import Firefox
from pages.login_page import LoginPage
import time


class ProcedimentoTesteLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Firefox()
        self.login_page = LoginPage(self.driver)
        

    def test_invalid_login(self):
        self.login_page.fill_credentials('coloca email aq', 'senha aq')
        self.login_page.perform_login()

        time.sleep(3)
        
        error_message = self.login_page.get_error_message()
        self.assertIn('E-mail, CPF, CNPJ ou senha incorretos', error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
