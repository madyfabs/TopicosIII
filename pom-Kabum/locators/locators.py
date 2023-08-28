from selenium.webdriver.common.by import By


class LoginLocators():
    field_login = (By.ID, 'login')
    field_password = (By.ID, 'password')
    button_login = (By.CLASS_NAME, 'IconLoginButton')
    error_message = (By.XPATH, "/html/body/div[1]/main/div/div/div/form/div[3]/div/span")
    button_favorites = (By.ID, 'linkFavoritosHeader')
    add_favorite = (By.ID,'IconHeart')
    button_account = (By.ID,'linkMinhaContaHeader')
    button_orders = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/main/div/div/div[2]/div/button")

class SearchLocators():
    field_search = (By.NAME, 'query')

class ProductPageLocators:
    
    button_add_to_cart = (By.CLASS_NAME, 'IconAddToCart')
    toast_notification = (By.CLASS_NAME, 'toast-notification')
    success_message = (By.XPATH, "//div[@class='toast-notification']/span")
    cart_icon = (By.CLASS_NAME, 'IconHeaderCart')
    product_page = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/section/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/a")
   
class TopBarLocators:
    department_menu = (By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div[1]")
    hardware_option = (By.XPATH, "/html/body/div[1]/header/div[2]/div[2]/div/div/div[1]/div/div/a[1]")
             
class MonteSeuPCLocators:
    button_overlap = (By.XPATH, "/html/body/div[1]/div[2]/div/button")
    processador_radio = (By.ID, 'productInputRadio-102248')
    placa_mae_radio = (By.ID, 'productInputRadio-100672')
    memoria_ram_radio = (By.ID, 'productInputRadio-110814')
    placa_video = (By.ID, 'productInputRadio-384635')
    ssd = (By.ID, 'productInputRadio-80632')
    hd = (By.ID,'productInputRadio-63735')
    cooler = (By.ID,'productInputRadio-130040')
    fonte = (By.ID,'productInputRadio-371160')
    gabinete = (By.ID,'productInputRadio-103743')
    monitor = (By.ID,'productInputRadio-99865')
    button_avancar1 = (By.XPATH, "/html/body/div[1]/footer/div/div[2]/div/div/button")
    button_avancar2 = (By.XPATH, "/html/body/div[1]/footer/div/div[2]/div/div[2]/button")
    
class SacPageLocators:
    button_sac = (By.ID, 'linkSacHeader')

class FAQFilterPageLocators:
    button_conduta = (By.CSS_SELECTOR, "div#__next div.fNZKVB div.sc-biOYyE a.cfESXT")
    button_cookies = (By.ID, 'onetrust-accept-btn-handler')
   
class Acessibilidade:
    button_access = (By.CSS_SELECTOR, 'button[aria-label="Abrir opções de acessibilidade"]')
    botao_access1 = (By.CSS_SELECTOR, 'a[href="/acessibilidade"]')
