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

def test_amazon_scroll_basic(setup):
    driver, driver_setup = setup
    func = FunctionsGeneric(driver)
    globalVar = InitConfig()
    # Obtiene la URL principal desde la configuración initConfig.json donde declaro todas las appsa
    url = globalVar.get('MainAppUrlBaseAmazon',)
    driver.get(url)

    # Paso 1: Teclear 'tenis nike' en el campo de búsqueda
    func.send_keys('BusquedaText', 'tenis nike')

    # Paso 2: Hacer clic en el botón de búsqueda
    func.click('BtnBusqueda')

    func.click('LinkMasVendidos')

    # Paso 3: Hacer scroll hacia abajo 100 píxeles
    func.scroll_bar_generic('down', 1000)


