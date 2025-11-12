# Reservas de Hotel - Sistema de Precios

Un proyecto para hacer reservas de hotel usando tres patrones de OOP: herencia, singleton y strategy. Basicamente es lo que nos pidieron para la tarea.

## Estructura del proyecto

```
reservas_hotel/
├── main.py                    # el script principal, ejecuta todo
├── modelos/
│   ├── alojamiento.py         # hotel y apartamento (dos tipos diferentes)
│   ├── reserva.py             # clase reserva (la usamos para guardar datos)
│   └── habitacion.py          # modelo habitacion (de verdad no lo usamos mucho)
├── configuracion/
│   └── configuracion_hotel.py  # aqui va la config general (singleton)
└── estrategias/
    ├── estrategia_precio.py   # estrategias de precio diferentes
    └── __init__.py
```

## Los tres patrones que pedían

### 1. Herencia y Polimorfismo
En `modelos/alojamiento.py` tenemos:
- `Alojamiento` es una clase base abstracta (como una plantilla)
- `Hotel` y `Apartamento` heredan de `Alojamiento`
- Ambas tienen `calcular_costo()` pero funcionan diferente
- En `main.py` vemos cómo ambas devuelven precios distintos cuando les pasas los mismos datos

### 2. Patrón Singleton
En `configuracion/configuracion_hotel.py`:
- `ConfiguracionHotel` es un singleton (solo existe una instancia)
- Guardamos la tarifa base y el modo del hotel
- Se puede acceder desde cualquier lado del código
- Si cambias la tarifa en un lado, se cambia en todos lados

### 3. Patrón Strategy
En `estrategias/estrategia_precio.py`:
- Tenemos `EstrategiaPrecio` (la interfaz)
- `PrecioEstandar` y `DescuentoLargaEstancia` son dos formas diferentes de calcular el precio
- En `main.py` vemos cómo cambiar la estrategia sin usar if/else

### 4. Todo junto en main.py
El main muestra cómo interactúan los tres patrones. Las clases del hotel usan estrategias y la config global.

## Cómo ejecutar

```powershell
# Primero activa el venv (si no lo hiciste ya)
 .venv/Scripts/Activate

# Luego ejecuta el main
 -m reservas_hotel.main
```

O si ya estás en la carpeta correcta:
```
python -m reservas_hotel.main
```

## Qué debería salir

Te va a mostrar:
1. La config global al principio
2. El costo de dos alojamientos con precio normal
3. El costo con descuento por larga estancia
4. Cómo cambiar la tarifa base afecta a todo

## Notas random

- Los imports usan el nombre del paquete completo para que funcione como módulo
- Si el alojamiento no tiene tarifa propia, usa la de la config global (eso es el singleton en acción)
- La estrategia se cambia dinámicamente, sin condiciones ni nada
- Podria haber persistencia en JSON o más validaciones, pero esto está ok para la tarea
