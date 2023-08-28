import unittest
from selenium import webdriver
from pages.top_bar import TopBar
import time


class ProcedimentoTesteFiltragem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.top_bar = TopBar(self.driver)

    def test_filter_department_hardware(self):
        self.top_bar.hover_department_menu()
        time.sleep(1)
        self.top_bar.select_hardware_option()
        
        time.sleep(1)
        self.assertEqual(self.driver.current_url, 'https://www.kabum.com.br/hardware')


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()