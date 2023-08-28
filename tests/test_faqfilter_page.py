import unittest
from selenium.webdriver import Firefox
from pages.faqfilter_page import FAQFilterPage
import time

class ProcedimentoTesteFAQFilterPage(unittest.TestCase):

    def setUp(self):
        self.driver = Firefox()
        self.faqfilter_page = FAQFilterPage(self.driver)

    def test_click_codigo_conduta_link(self):
        self.faqfilter_page.get_button_cookies()
        time.sleep(3)
        self.faqfilter_page.get_codigo_conduta()

        time.sleep(10)
        self.assertEqual(self.driver.current_url, 'https://www.kabum.com.br/codigo-conduta')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()