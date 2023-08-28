from pages.base_page import BasePage
from locators.locators import MonteSeuPCLocators

class BuildPC(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        driver.get('https://www.kabum.com.br/monteoseupc')

    def remove_overlap(self):
        self.click(MonteSeuPCLocators.button_overlap)
        
    def add_processor(self):
        self.click(MonteSeuPCLocators.processador_radio)

    def add_placa_mae(self):
        self.click(MonteSeuPCLocators.placa_mae_radio)

    def add_ram(self):
        self.click(MonteSeuPCLocators.memoria_ram_radio)
    
    def add_placa_video(self):
        self.click(MonteSeuPCLocators.placa_video)

    def add_ssd(self):
        self.click(MonteSeuPCLocators.ssd)

    
    def add_hd(self):
        self.click(MonteSeuPCLocators.hd)
    

    def add_cooler(self):
        self.click(MonteSeuPCLocators.cooler)
        
    def add_fonte(self):
        self.click(MonteSeuPCLocators.fonte)
        
    def add_gabinete(self):
        self.click(MonteSeuPCLocators.gabinete)

    def add_monitor(self):
        self.click(MonteSeuPCLocators.monitor)
    
    def inicia(self):
        self.click(MonteSeuPCLocators.button_avancar1)

    def avancar(self):
        self.click(MonteSeuPCLocators.button_avancar2)
       
  
    
    
    
   
   