from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class Reserva:
    cliente: str
    alojamiento: str
    fecha_inicio: date
    noches: int

    def fecha_fin(self) -> date:
        return self.fecha_inicio + timedelta(days=self.noches)

    def __str__(self) -> str:
        return f"Reserva(cliente={self.cliente}, alojamiento={self.alojamiento}, noches={self.noches})"
