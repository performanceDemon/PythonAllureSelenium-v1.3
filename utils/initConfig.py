import json
import os

class InitConfig:
    # Ruta relativa del archivo JSON
    CONFIG_FILE_PATH = 'InitConfig.json'

    def __init__(self):
        # Resuelve la ruta del archivo JSON usando la ruta relativa
        config_path = os.path.join(os.path.dirname(__file__), self.CONFIG_FILE_PATH)
        self._config = self.load_config(config_path)

    def load_config(self, json_file_path):
        """Carga la configuración desde un archivo JSON."""
        with open(json_file_path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        """Obtiene un valor de la configuración basado en la clave."""
        return self._config.get(key, default)

    def __getattr__(self, key):
        """Permite el acceso dinámico a las variables de configuración."""
        if key in self._config:
            return self._config[key]
        raise AttributeError(f"'InitConfig' object has no attribute '{key}'")
