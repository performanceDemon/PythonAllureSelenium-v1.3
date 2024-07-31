import pytest
from utils.InicializarDriver import InicializarDriver
from utils.FunctionsGeneric import FunctionsGeneric
from utils.initConfig import InitConfig

@pytest.fixture(scope='module')
def setup():
    driver_setup = InicializarDriver()
    driver = driver_setup.get_driver()
    yield driver, driver_setup
    driver.quit()

def test_fail_login_validMSG(setup):
    driver, driver_setup = setup
    func = FunctionsGeneric(driver)
    globalVar = InitConfig()
    # Obtiene la URL principal desde la configuración initConfig.json donde declaro todas las appsa
    url = globalVar.get('MainAppUrlBaseAmazon',)
    driver.get(url)

    func.click('BtnIniciarSesion')
##esta funcion logea en un paso y valida el mensaje de error de manera generica

    func.login1step('InputEmailLogin','isaac@fake.com',
                    'BtnLoginContinuar1',
                    'ValMensaajeError','No pudimos encontrar una cuenta con esa dirección de correo electrónico')

    func.take_screenshot('errorloginAmazon')