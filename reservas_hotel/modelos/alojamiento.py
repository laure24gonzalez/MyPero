from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from reservas_hotel.estrategias import EstrategiaPrecio
from reservas_hotel.configuracion.configuracion_hotel import ConfiguracionHotel

# esto es basicamente la clase plantilla para todos los alojamientos
# hotel y apartamento van a heredar de aca


class Alojamiento(ABC):
    # clase base para hoteles, apartamentos, cabañas, lo que sea
    # los metodos abstract son los que tienen que implementar todas las subclases

    def __init__(self, nombre: str, ubicacion: str, tarifa_por_noche: Optional[float] = None) -> None:
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tarifa_por_noche = tarifa_por_noche

    @abstractmethod
    def calcular_costo(self, noches: int, estrategia: EstrategiaPrecio) -> float:
        # cada tipo de alojamiento calcula el costo a su manera
        pass

    @abstractmethod
    def mostrar_detalle(self) -> str:
        # cada uno muestra sus detalles de forma diferente
        pass


class Hotel(Alojamiento):
    # heredamos de Alojamiento y le sumamos cosas de hotel
    def __init__(self, nombre: str, ubicacion: str, tarifa_por_noche: Optional[float], incluye_desayuno: bool = False, impuesto: float = 0.12) -> None:
        super().__init__(nombre, ubicacion, tarifa_por_noche)
        self.incluye_desayuno = incluye_desayuno
        self.impuesto = impuesto

    def calcular_costo(self, noches: int, estrategia: EstrategiaPrecio) -> float:
        # el hotel usa la estrategia pero le suma el desayuno y el impuesto
        tarifa = self.tarifa_por_noche if self.tarifa_por_noche is not None else ConfiguracionHotel().get("tarifa_base", 100.0)
        subtotal = estrategia.calcular(float(tarifa), noches)
        if self.incluye_desayuno:
            subtotal += 10.0 * noches  # agregar costo del desayuno
        total = subtotal * (1 + self.impuesto)  # aplicar impuesto del hotel
        return round(total, 2)

    def mostrar_detalle(self) -> str:
        desayuno = "sí" if self.incluye_desayuno else "no"
        tarifa = self.tarifa_por_noche if self.tarifa_por_noche is not None else ConfiguracionHotel().get("tarifa_base", 100.0)
        return f"Hotel '{self.nombre}' en {self.ubicacion} - tarifa ${tarifa}/noche, desayuno={desayuno}"


class Apartamento(Alojamiento):
    # parecido al hotel pero sin impuesto, tiene costo de limpieza
    def __init__(self, nombre: str, ubicacion: str, tarifa_por_noche: Optional[float], limpieza_unica: float = 30.0) -> None:
        super().__init__(nombre, ubicacion, tarifa_por_noche)
        self.limpieza_unica = limpieza_unica

    def calcular_costo(self, noches: int, estrategia: EstrategiaPrecio) -> float:
        # el apartamento solo suma la limpieza al resultado de la estrategia
        tarifa = self.tarifa_por_noche if self.tarifa_por_noche is not None else ConfiguracionHotel().get("tarifa_base", 100.0)
        subtotal = estrategia.calcular(float(tarifa), noches)
        subtotal += self.limpieza_unica  # una sola vez, no por noche
        return round(subtotal, 2)

    def mostrar_detalle(self) -> str:
        tarifa = self.tarifa_por_noche if self.tarifa_por_noche is not None else ConfiguracionHotel().get("tarifa_base", 100.0)
        return f"Apartamento '{self.nombre}' en {self.ubicacion} - tarifa ${tarifa}/noche, limpieza ${self.limpieza_unica}"
