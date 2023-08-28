from pages.base_page import BasePage
from locators.locators import LoginLocators



class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        driver.get('https://www.kabum.com.br/login')

    def fill_credentials(self, login, password):
        self.enter_text(LoginLocators.field_login, login)
        self.enter_text(LoginLocators.field_password, password)

    def perform_login(self):
        self.click(LoginLocators.button_login)

    def get_error_message(self):
        return self.find_element(LoginLocators.error_message).text
    
    def get_favorites(self):
        self.click(LoginLocators.button_favorites)
    
    def add_favorites(self):
        self.click(LoginLocators.add_favorite)

    def get_account_info(self):
        self.click(LoginLocators.button_account)

    def get_orders(self):
        self.click(LoginLocators.button_orders)    