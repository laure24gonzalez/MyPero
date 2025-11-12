from reservas_hotel.modelos.alojamiento import Hotel, Apartamento
from reservas_hotel.configuracion.configuracion_hotel import ConfiguracionHotel
from reservas_hotel.estrategias import PrecioEstandar, DescuentoLargaEstancia, EstrategiaPrecio

# esto es un contexto para la estrategia
# basicamente es un objeto que guarda cual estrategia usar
# y permite cambiarla sin que el resto del codigo se entere


class CalculadorPrecio:
    # una clase que es responsable de calcular precios usando estrategias

    def __init__(self, estrategia: EstrategiaPrecio) -> None:
        # empezar con una estrategia
        self.estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaPrecio) -> None:
        # cambiar la estrategia dinamicamente (sin if/else)
        self.estrategia = estrategia

    def calcular(self, alojamiento: Hotel | Apartamento, noches: int) -> float:
        # le pedimos al alojamiento que calcule usando la estrategia que tenemos ahora
        return alojamiento.calcular_costo(noches, self.estrategia)


def main() -> None:
    # iniciamos la config global del hotel (esto es el singleton que nos pidieron)
    # no importa de dónde se accede, siempre es la misma instancia
    cfg = ConfiguracionHotel(tarifa_base=100.0, modo="desarrollo")
    print("Configuración global inicial:", cfg.all())

    # creamos dos tipos de alojamientos diferentes (herencia + polimorfismo)
    # el hotel hereda de alojamiento, igual que el apartamento
    # pero cada uno calcula el costo de forma distinta
    alojamientos: list[Hotel | Apartamento] = [
        Hotel("Gran Sol", "Mar del Plata", tarifa_por_noche=None, incluye_desayuno=True),
        Apartamento("Depto Central", "Buenos Aires", tarifa_por_noche=60.0, limpieza_unica=25.0),
    ]

    # definimos dos estrategias de precio (esto es el patrón strategy)
    # sin estrategias iríamos a usar if/else... nah, pas!
    estandar = PrecioEstandar()
    descuento = DescuentoLargaEstancia(umbral=7, descuento=0.15)

    # el contexto guarda la estrategia actual
    contexto = CalculadorPrecio(estandar)

    noches = 5
    print("\n-- Cálculo con estrategia estándar --")
    # polimorfismo en acción: ambos tipos llaman a calcular_costo pero se comportan distinto
    for a in alojamientos:
        print(a.mostrar_detalle())
        print(f"Costo para {noches} noches: ${contexto.calcular(a, noches):.2f}\n")

    # ahora cambiamos la estrategia sin tocar nada más
    # esto es lo que hace potente el patrón strategy
    contexto.set_estrategia(descuento)
    print("-- Cálculo con estrategia descuento larga estancia --")
    for a in alojamientos:
        print(a.mostrar_detalle())
        print(f"Costo para {noches} noches: ${contexto.calcular(a, noches):.2f}\n")

    # cambiamos el singleton de configuración y eso afecta todos los cálculos
    # cualquier alojamiento que use la tarifa base va a recalcular automáticamente
    cfg.set("tarifa_base", 130.0)
    print("-- Después de cambiar tarifa_base en configuración global --")
    for a in alojamientos:
        print(a.mostrar_detalle())
        print(f"Costo para {noches} noches: ${contexto.calcular(a, noches):.2f}\n")


if __name__ == "__main__":
    main()
