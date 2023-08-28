from pages.base_page import BasePage
from locators.locators import SacPageLocators


class SACPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://www.kabum.com.br/')

    def get_sac_icon(self):
        self.click(SacPageLocators.button_sac)
        