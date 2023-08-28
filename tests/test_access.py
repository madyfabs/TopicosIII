import unittest
from selenium.webdriver import Firefox
from pages.acessibilidade_page import Access
import time

class ProcedimentoTesteAcessibilidade(unittest.TestCase):

    def setUp(self):
        self.driver = Firefox()
        self.acessibilidade_page = Access(self.driver)

    def test_click_codigo_conduta_link(self):
        self.acessibilidade_page.get_access_button()
        self.acessibilidade_page.get_access_button2()

        time.sleep(5)
        self.assertEqual(self.driver.current_url, 'https://www.kabum.com.br/acessibilidade')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()