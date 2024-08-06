# utils/custom_exceptions.py

class ElementNotFoundException(Exception):
    """Excepción personalizada para elementos no encontrados."""
    def __init__(self, message="Elemento no encontrado."):
        self.message = message
        super().__init__(self.message)

class TimeoutException(Exception):
    """Excepción personalizada para tiempos de espera excedidos."""
    def __init__(self, message="Tiempo de espera excedido."):
        self.message = message
        super().__init__(self.message)

class LoginFailedException(Exception):
    """Excepción personalizada para fallos en el login."""
    def __init__(self, message="Falló el login."):
        self.message = message
        super().__init__(self.message)
