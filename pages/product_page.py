from pages.base_page import BasePage
from locators.locators import ProductPageLocators

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        driver.get('https://www.kabum.com.br/produto/401272/placa-de-video-rtx-3060-ti-1-click-oc-plus-galax-nvidia-geforce-8-gb-gddr6x-dlss-ray-tracing-36ism6md2kcv')
        

    def add_product_to_cart(self):
        self.click(ProductPageLocators.button_add_to_cart)
        self.wait_for_element_visibility(ProductPageLocators.toast_notification)

    def remove_from_cart(self):
        self.click(ProductPageLocators.button_add_to_cart)

    def get_item_from_cart(self):
        self.click(ProductPageLocators.product_page)
    
    def get_success_message(self):
        return self.find_element(ProductPageLocators.success_message).text
    
    def get_cart_icon_text(self):
        return self.find_element(ProductPageLocators.cart_icon).text
    
    def go_to_cart(self):
        self.click(ProductPageLocators.cart_icon)