from pages.base_page import BasePage
from locators.locators import FAQFilterPageLocators


class FAQFilterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.kabum.com.br/faq')

    def get_codigo_conduta(self):
        self.click(FAQFilterPageLocators.button_conduta)
    
    def get_button_cookies(self):
        self.click(FAQFilterPageLocators.button_cookies)