import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException
from utils.custom_exceptions import ElementNotFoundException, TimeoutException, LoginFailedException
import allure
from datetime import datetime



class FunctionsGeneric:
    def __init__(self, driver: WebDriver, config_file: str = 'DOMpages/DOM-Amazon.json', timeout=5):
        self.driver = driver
        # Resuelve la ruta del archivo JSON usando la ruta relativa
        config_path = os.path.join(os.path.dirname(__file__), '..', config_file)
        self.locators = self.load_locators(config_path)
        self.timeout = timeout
        self.screenshots_folder = 'reports/ScreenShotEvidence/'

        # Asegúrate de que la carpeta de capturas de pantalla exista
        if not os.path.exists(self.screenshots_folder):
            os.makedirs(self.screenshots_folder)

    def load_locators(self, json_file_path: str):
        """Carga los localizadores desde un archivo JSON."""
        with open(json_file_path, 'r') as file:
            return json.load(file)

    def get_locator(self, name: str):
        """Obtiene el localizador basado en un nombre genérico."""
        locator_info = self.locators.get(name)
        if not locator_info:
            raise ValueError(f"Locator for '{name}' not found")

        by_type = locator_info.get("GetFielBy")
        value = locator_info.get("ValueToFind")

        if by_type == "xpath":
            by = By.XPATH
        elif by_type == "id":
            by = By.ID
        elif by_type == "css":
            by = By.CSS_SELECTOR
        elif by_type == "href":
            by = By.LINK_TEXT
        else:
            raise ValueError(f"Locator type '{by_type}' is not supported")

        return by, value

    def get_element(self, name: str):
        """Obtiene un elemento basado en un nombre genérico."""
        by, value = self.get_locator(name)
        return self.driver.find_element(by, value)

    def click(self, name: str):
        """Realiza clic en un elemento basado en un nombre genérico."""
        by, value = self.get_locator(name)
        try:
         element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, value))
         )
         element.click()
        except ElementClickInterceptedException:
            raise ElementClickInterceptedException(
               f"No se pudo hacer clic en el elemento '{name}' por que no lo encontro {value}")
        except Exception:
           raise TimeoutException(f"No se pudo hacer clic en el elemento '{name}' usando {by} con valor {value}")

    def send_keys(self, name: str, keys: str):
        """Envía teclas a un elemento basado en un nombre genérico."""
        by, value = self.get_locator(name)
        try:
         element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, value))
         )
         element.send_keys(keys)
        except Exception:
           raise TimeoutException(f"No se pudo enviar las teclas al elemento '{name}' con valor {value}")

    def scroll_bar_generic(self, direction: str, value: int = 500):
        """
        Desplaza la barra de desplazamiento de la página.
        :param direction: Dirección del desplazamiento. Puede ser 'down', 'up', 'left', 'right'.
        :param value: Valor de desplazamiento en píxeles.
        """
        if direction not in ['down', 'up', 'left', 'right']:
            raise ValueError("Direction must be one of: 'down', 'up', 'left', 'right'")

        if direction == 'down':
            self.driver.execute_script(f"window.scrollBy(0, {value});")
        elif direction == 'up':
            self.driver.execute_script(f"window.scrollBy(0, -{value});")
        elif direction == 'left':
            self.driver.execute_script(f"window.scrollBy(-{value}, 0);")
        elif direction == 'right':
            self.driver.execute_script(f"window.scrollBy({value}, 0);")

    def login(self, username: str, password: str, username_field_name: str, password_field_name: str,
              login_button_name: str):
        """Realiza el proceso de login."""
        # Espera explícita para que el campo de nombre de usuario sea visible
        try:
            by, value = self.get_locator(username_field_name)
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            self.send_keys(username_field_name, username)

            # Espera explícita para que el campo de contraseña sea visible
            by, value = self.get_locator(password_field_name)
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            self.send_keys(password_field_name, password)

            # Espera explícita para que el botón de login sea clicable
            by, value = self.get_locator(login_button_name)
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            self.click(login_button_name)
        except ElementClickInterceptedException:
            raise ElementClickInterceptedException(
               f"No se pudo hacer clic en el elemento '{login_button_name}' porque otro elemento lo interceptó")
        except Exception:
            raise TimeoutException(f"No se pudo hacer clic en el elemento '{login_button_name}' usando valor {value}")
        except Exception:
            raise TimeoutException(f"No se pudo enviar las teclas al elemento '{username_field_name}' ")

    def login1step(self, username_field_name: str, username: str, login_button_name: str, alert_element_name: str, expected_message: str):
        """Realiza el proceso de login de un paso y valida el mensaje de error."""
        # Espera explícita para que el campo de nombre de usuario sea visible

        by, value = self.get_locator(username_field_name)
        try:
           WebDriverWait(self.driver, self.timeout).until(
               EC.visibility_of_element_located((by, value))
           )
           self.send_keys(username_field_name, username)

           # Hace clic en el botón de login
           self.click(login_button_name)

           # Espera explícita para que el elemento de alerta sea visible
           by, value = self.get_locator(alert_element_name)
           alert_element = WebDriverWait(self.driver, self.timeout).until(
               EC.visibility_of_element_located((by, value))
           )

           # Valida el mensaje del elemento de alerta
           actual_message = alert_element.text
           assert actual_message == expected_message, f"Expected message: '{expected_message}', but got: '{actual_message}'"


        except ElementClickInterceptedException:
           raise ElementClickInterceptedException(
               f"No se pudo hacer clic en el elemento '{login_button_name}' porque otro elemento lo interceptó")
        except Exception:
           raise TimeoutException(f"No se pudo hacer clic en el elemento '{login_button_name}' usando valor {value}")


    def wait_for_element(self, name: str):
        """Espera a que un elemento esté presente en la página."""
        try:
            by, value = self.get_locator(name)
            WebDriverWait(self.driver, self.timeout).until(
                    EC.presence_of_element_located((by, value))
                )
        except Exception:
           raise TimeoutException(f"se espero hasta {self.timeout}  segundo y no aparecio el elemento'{value}' ")

    def is_element_visible(self, name: str) -> bool:
        """Verifica si un elemento es visible en la página."""
        try:
            by, value = self.get_locator(name)
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except Exception:
            raise TimeoutException(f"No se visualiza el elemento '{value}' ")


    def select_from_dropdown(self, name: str, value: str):
        """Selecciona un valor de un menú desplegable."""
        by, value_locator = self.get_locator(name)
        dropdown = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, value_locator))
        )
        select = Select(dropdown)
        select.select_by_visible_text(value)

    def handle_alert(self, action: str = 'accept'):
        """Maneja las alertas del navegador."""
        alert = WebDriverWait(self.driver, self.timeout).until(
            EC.alert_is_present()
        )
        if action == 'accept':
            alert.accept()
        elif action == 'dismiss':
            alert.dismiss()
        else:
            raise ValueError(f"Action '{action}' is not supported")

    def take_screenshot(self, base_name: str, file_format: str = 'png'):
        """Toma una captura de pantalla con un nombre único y formato especificado, y la adjunta a Allure."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{base_name}_{timestamp}.{file_format}"
        file_path = os.path.join(self.screenshots_folder, file_name)

        # Toma la captura de pantalla
        screenshot = self.driver.get_screenshot_as_png()
        with open(file_path, 'wb') as file:
            file.write(screenshot)

        # Adjunta la captura de pantalla a Allure
        allure.attach(
            name=base_name,
            body=screenshot,
            attachment_type=allure.attachment_type.PNG
        )
        print(f"Screenshot saved as {file_path} and attached to Allure report.")

