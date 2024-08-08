import pytest
from utils.NavegadorInit import BaseTest, navegador_setup

@pytest.mark.usefixtures("navegador_setup")
@pytest.mark.config_key('DOMHomeEBAY')

class TestPaginador4EBAY(BaseTest):
    def test_ebay_paginador4(self):
        self.navegador.iniciar_navegador('MainAppUrlEBAY')
    # Paso 1: Teclear 'tenis nike' en el campo de búsqueda
        self.navegador.func.send_keys('CampoBusquedaTXT', 'adidas running')

    # Paso 2: Hacer clic en el botón de búsqueda
        self.navegador.func.click('BtnBusqueda')
        #self.navegador.func.isvisible('BtnBusqueda')


    # Paso 3: Hacer scroll hacia abajo 100 píxeles
        self.navegador.func.scroll_bar_generic('down', 1000)
        self.navegador.func.scroll_bar_generic('down', 1000)
        self.navegador.func.scroll_bar_generic('down', 7000)

        self.navegador.func.wait_for_element('paginador4')
        self.navegador.func.click('paginador4')
        self.navegador.func.take_screenshot('pagina4resultados')