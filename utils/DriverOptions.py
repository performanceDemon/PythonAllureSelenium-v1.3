# driverOptions.py
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class DriverOptions:
    def get_chrome_options(self):
        chrome_options = ChromeOptions()
        # Puedes agregar configuraciones específicas aquí
        chrome_options.add_argument("--start-maximized")
        #chrome_options.add_argument("--headless")  # Ejecuta en modo headless
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        return chrome_options

    def get_edge_options(self):
        edge_options = EdgeOptions()
        # Puedes agregar configuraciones específicas aquí
        edge_options.add_argument("--start-maximized")
        return edge_options
