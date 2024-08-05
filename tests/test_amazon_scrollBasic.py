
import pytest
from utils.NavegadorInit import BaseTest, navegador_setup


@pytest.mark.usefixtures("navegador_setup")
@pytest.mark.config_key('amazonPagecompras')
class TestAmazonScroll(BaseTest):
    def test_amazon_scroll_basic(self):
        self.navegador.iniciar_navegador('MainAppUrlBaseAmazon')
    # Paso 1: Teclear 'tenis nike' en el campo de búsqueda
        self.navegador.func.send_keys('BusquedaText', 'tenis nike')

    # Paso 2: Hacer clic en el botón de búsqueda
        self.navegador.func.click('BtnBusqueda')

        self.navegador.func.click('LinkMasVendidos')

    # Paso 3: Hacer scroll hacia abajo 100 píxeles
        self.navegador.func.scroll_bar_generic('down', 1000)


