import unittest
from selenium.webdriver import Firefox
from pages.sac_page import SACPage
import time

class ProcedimentoTesteSACPage(unittest.TestCase):

    def setUp(self):
        self.driver = Firefox()
        self.sac_page = SACPage(self.driver)

    def test_click_sac_link(self):
        self.sac_page.get_sac_icon()
        self.assertEqual(self.driver.current_url, 'https://www.kabum.com.br/faq')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()