# utils/NavegadorInit.py

import pytest
from utils.InicializarDriver import InicializarDriver
from utils.FunctionsGeneric import FunctionsGeneric
from utils.initConfig import InitConfig

class NavegadorInit:
    def __init__(self):
        self.driver_setup = InicializarDriver()
        self.driver = self.driver_setup.get_driver()
        self.func = FunctionsGeneric(self.driver)
        self.globalVar = InitConfig()

    def iniciar_navegador(self, nombre_url):
        # Obtiene la URL desde la configuración initConfig.json donde declaro todas las apps
        url = self.globalVar.get(nombre_url)
        self.driver.get(url)

    def cerrar_navegador(self):
        self.driver.quit()

@pytest.fixture(scope='class')
def navegador_setup(request):
    navegador = NavegadorInit()
    request.cls.navegador = navegador
    yield
    navegador.cerrar_navegador()

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, navegador_setup):
        pass
