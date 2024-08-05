# tests/test_fail_login.py

import pytest
from utils.NavegadorInit import BaseTest, navegador_setup


@pytest.mark.usefixtures("navegador_setup")
@pytest.mark.config_key('amazonPagecompras')
class TestFailLogin(BaseTest):

    def test_fail_login_validMSG(self):
        # Iniciar navegador y navegar a la URL principal
        self.navegador.iniciar_navegador('MainAppUrlBaseAmazon')

        # Hace clic en el botón de iniciar sesión
        self.navegador.func.click('BtnIniciarSesion')

        # Esta función logea en un paso y valida el mensaje de error de manera genérica
        self.navegador.func.login1step('InputEmailLogin', 'isaac@fake.com',
                                       'BtnLoginContinuar1',
                                       'ValMensaajeError',
                                       'No pudimos encontrar una cuenta con esa dirección de correo electrónico')

        # Toma una captura de pantalla en caso de error
        self.navegador.func.take_screenshot('errorloginAmazon')
