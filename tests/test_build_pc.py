import unittest
from selenium.webdriver import Firefox
from pages.build_pc import BuildPC
import time

class ProcedimentoTesteMontaPC(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.build_pc = BuildPC(self.driver)

    def test_build(self):
        
        self.build_pc.remove_overlap()
        self.build_pc.add_processor()
        self.build_pc.inicia()

        time.sleep(1)
        
        self.build_pc.add_placa_mae()
        time.sleep(1)
        self.build_pc.avancar()

        self.build_pc.add_ram()
        time.sleep(1)
        self.build_pc.avancar()

        self.build_pc.add_placa_video()
        time.sleep(1)
        self.build_pc.avancar()

        self.build_pc.add_ssd()
        time.sleep(1)
        self.build_pc.avancar()
        
        self.build_pc.add_hd()
        time.sleep(1)
        self.build_pc.avancar()

        self.build_pc.add_cooler()
        time.sleep(1)
        self.build_pc.avancar()

        self.build_pc.add_fonte()
        time.sleep(1)
        self.build_pc.avancar()

        self.build_pc.add_gabinete()
        time.sleep(1)
        self.build_pc.avancar()
        
        self.build_pc.add_monitor()
        time.sleep(1)
        self.build_pc.avancar()

        time.sleep(2)

        self.assertEqual(self.driver.current_url, 'https://www.kabum.com.br/monteoseupc/resumo')
        
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
