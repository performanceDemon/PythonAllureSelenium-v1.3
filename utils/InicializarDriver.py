import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.initConfig import InitConfig
from utils.DriverOptions import DriverOptions


class InicializarDriver:
    def __init__(self):
        # Cargar la configuración
        self.config = InitConfig()
        self.options = DriverOptions()
        self.driver = self.create_driver()

    def create_driver(self):
        browser = self.config.get('browser', 'chrome').lower()  # Valor por defecto es 'chrome'

        # Obtener la ruta del directorio de drivers desde el JSON
        resource_folder = self.config.get('resourceFolder', 'resources/drivers/')
        driver_path = os.path.join(os.path.dirname(__file__), '..', resource_folder.lstrip('/'))

        # Verificar que la ruta del driver sea correcta
        if not os.path.exists(driver_path):
            raise FileNotFoundError(f"El directorio de drivers no se encuentra en {driver_path}")

        if browser == 'chrome':
            chrome_options = self.options.get_chrome_options()
            chrome_driver_path = os.path.join(driver_path, 'chromedriver')
            if not os.path.exists(chrome_driver_path):
                raise FileNotFoundError(f"El archivo del driver no se encuentra en {chrome_driver_path}")
            service = ChromeService(executable_path=chrome_driver_path)
            return webdriver.Chrome(service=service, options=chrome_options)
        elif browser == 'edge':
            edge_options = self.options.get_edge_options()
            edge_driver_path = os.path.join(driver_path, 'msedgedriver')
            if not os.path.exists(edge_driver_path):
                raise FileNotFoundError(f"El archivo del driver no se encuentra en {edge_driver_path}")
            service = EdgeService(executable_path=edge_driver_path)
            return webdriver.Edge(service=service, options=edge_options)
        else:
            raise ValueError(f"Browser {browser} is not supported")

    def get_driver(self):
        return self.driver
