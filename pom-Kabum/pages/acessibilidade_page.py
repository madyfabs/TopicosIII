from pages.base_page import BasePage
from locators.locators import Acessibilidade

class Access(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.kabum.com.br/')

    def get_access_button(self):
        self.click(Acessibilidade.button_access)

    def get_access_button2(self):
        self.click(Acessibilidade.botao_access1)
        