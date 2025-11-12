from dataclasses import dataclass


@dataclass
class Habitacion:
    numero: int
    tipo: str
    tarifa_por_noche: float

    def __str__(self) -> str:
        return f"Habitacion(numero={self.numero}, tipo={self.tipo}, tarifa={self.tarifa_por_noche})"
