
import pytest
from utils.NavegadorInit import BaseTest, navegador_setup

@pytest.mark.usefixtures("navegador_setup")
@pytest.mark.config_key('DOMMercadoLibre')
class TestBuscarTopMercadoLibre(BaseTest):

    def test_merrcadoLibre_busquedaTop(self):
        self.navegador.iniciar_navegador('MercadoLibreURL')
    # Paso 1: Teclear 'tenis nike' en el campo de búsqueda
        self.navegador.func.send_keys('CampoBusquedaTXT', 'reebok mujer')

    # Paso 2: Hacer clic en el botón de búsqueda
        self.navegador.func.click('BtnBusqueda')
        #self.navegador.func.isvisible('BtnBusqueda')


    # Paso 3: Hacer scroll hacia abajo 100 píxeles
        self.navegador.func.scroll_bar_generic('down', 1000)
        self.navegador.func.scroll_bar_generic('down', 1000)
        self.navegador.func.scroll_bar_generic('down', 7000)

        self.navegador.func.wait_for_element('linkNanotenis')
        self.navegador.func.click('linkNanotenis')
        self.navegador.func.take_screenshot('resultadoBusqueda2')

