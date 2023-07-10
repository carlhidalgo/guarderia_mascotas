# Prueba 3
from funciones import *

# Menú principal

opcionIngresada = -1
identificadorDisponible = 1
while opcionIngresada != 4:
    print("Bienvenido a la guardería Mascota Segura")
    print("Menú de opciones")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Retirarse")
    print("4. Salir")

    opcionIngresada = validarOpcion(4)

    if opcionIngresada == 1:
        grabar(identificadorDisponible)
    elif opcionIngresada == 2:
        buscar()
    elif opcionIngresada == 3:
        retirarse()
    else:
        salir()