import threading
from typing import Any, Dict

# singleton significa que solo hay una instancia en todo el programa
# util para compartir config entre todos lados


class ConfiguracionHotel:
    # aqui guardamos los valores globales del hotel
    # se crea una sola vez y todos acceden a la misma instancia

    _lock = threading.Lock()  # para que funcione bien con threads
    _instance = None
    _values: Dict[str, Any]

    def __new__(cls, **kwargs: Any):
        # esto es el "truco" del singleton
        # si ya existe una instancia, devolvemos esa
        # si no, creamos una nueva
        if cls._instance is None:
            with cls._lock:  # asegurar que solo un thread cree la instancia
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._values = {
                        "tarifa_base": 100.0,
                        "modo": "produccion",
                    }
                    # inicializar con kwargs si los hay
                    cls._instance._values.update(kwargs)
        return cls._instance

    def get(self, key: str, default: Any = None) -> Any:
        # obtener un valor de la config
        return self._values.get(key, default)

    def set(self, key: str, value: Any) -> None:
        # cambiar un valor de la config
        self._values[key] = value

    def all(self) -> Dict[str, Any]:
        # devolver todos los valores
        return dict(self._values)
