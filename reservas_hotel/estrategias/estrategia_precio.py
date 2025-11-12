from abc import ABC, abstractmethod

# esto son las estrategias para calcular precios
# la idea es poder cambiar como se calcula sin usar if/else


class EstrategiaPrecio(ABC):
    # interfaz que definen todas las estrategias
    @abstractmethod
    def calcular(self, tarifa_base: float, noches: int) -> float:
        # todas tienen que implementar este metodo
        raise NotImplementedError()


class PrecioEstandar(EstrategiaPrecio):
    # la estrategia mas simple: tarifa * noches, nada mas
    def calcular(self, tarifa_base: float, noches: int) -> float:
        return tarifa_base * noches


class DescuentoLargaEstancia(EstrategiaPrecio):
    # si te quedas muchos días, te hacemos descuento
    def __init__(self, umbral: int = 7, descuento: float = 0.1):
        self.umbral = umbral  # cuantos días minimo para descuento
        self.descuento = descuento  # que porcentaje es el descuento

    def calcular(self, tarifa_base: float, noches: int) -> float:
        subtotal = tarifa_base * noches
        if noches >= self.umbral:
            # si se queda mucho, le bajamos el precio
            subtotal *= (1 - self.descuento)
        return subtotal
