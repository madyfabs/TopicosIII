from selenium.webdriver.common.action_chains import ActionChains
from locators.locators import TopBarLocators
from pages.base_page import BasePage

class TopBar(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.kabum.com.br/')

    def hover_department_menu(self):
        department_menu = self.driver.find_element(*TopBarLocators.department_menu)
        action = ActionChains(self.driver)
        action.move_to_element(department_menu).perform()

    def select_hardware_option(self):
        hardware_option = self.driver.find_element(*TopBarLocators.hardware_option)
        hardware_option.click()
