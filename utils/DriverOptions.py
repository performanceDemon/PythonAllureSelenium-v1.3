# driverOptions.py
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class DriverOptions:
    def get_chrome_options(self):
        chrome_options = ChromeOptions()
        # Puedes agregar configuraciones específicas aquí
        chrome_options.add_argument("--start-maximized")
        return chrome_options

    def get_edge_options(self):
        edge_options = EdgeOptions()
        # Puedes agregar configuraciones específicas aquí
        edge_options.add_argument("--start-maximized")
        return edge_options
