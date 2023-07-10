# Validaciones

def validarNombre(minLetras, tipoNombre):
    nombreIngresado = ""
    while len(nombreIngresado) < minLetras:
        try:
            if tipoNombre == 0:
                nombreIngresado = input("Ingrese su nombre: ")
            else:
                nombreIngresado = input("Ingrese el nombre de su mascota: ")
            nombreIngresado = nombreIngresado.strip()
            assert nombreIngresado.isalpha()
        except:
            print("El nombre no debe contener espacios, números o caracteres especiales")
            nombreIngresado = ""
        else:
            if len(nombreIngresado) < minLetras:
                print("El nombre debe tener un mínimo de", minLetras, "letras")
    return nombreIngresado

def validarOpcion(nroOpciones):
    opcionIngresada = 0
    while opcionIngresada > nroOpciones or opcionIngresada < 1:
        try:
            opcionIngresada = int(input("Ingrese su opción: "))
        except:
            print("Debe ingresar un número entero")
        else:
            if (opcionIngresada > nroOpciones or opcionIngresada < 1):
                print("Opción inválida")
    return opcionIngresada

def validarRut():
    rutIngresado = ""
    while len(rutIngresado) < 7 or len(rutIngresado) > 8:
        try:
            rutIngresado = input("Ingrese su rut: ")
            rutIngresado = rutIngresado.strip()
            assert rutIngresado.isdigit()
        except:
            print("El rut no debe contener puntos, guiones o letras")
            rutIngresado = ""
        else:
            if len(rutIngresado) < 7 or len(rutIngresado) > 8:
                print("El rut debe contener entre 7 y 8 dígitos")
    return int(rutIngresado)

def validarDigitoVerificador():
    digitoVerificador = ""
    while not(digitoVerificador.isdigit()) and digitoVerificador != "k":
        try:
            digitoVerificador = input("Ingrese su dígito verificador: ")
            digitoVerificador = digitoVerificador.strip()
            assert len(digitoVerificador) == 1
        except:
            print("El dígito verificador no puede contene más de un dígito")
            digitoVerificador = ""
        else:
            if not(digitoVerificador.isdigit()) and digitoVerificador != "k":
                print("El dígito verificador solo puede ir de 0 a 9 o ser una K")
    return digitoVerificador

def validarDias():
    diasIngresado = -1
    while diasIngresado < 1:
        try:
            diasIngresado = int(input("Ingrese la cantidad de días a solicitar: "))
        except:
            print("Debe ingresar un número entero")
        else:
            if (diasIngresado < 1):
                print("No puede ingresar una cantidad negativa o cero")
    return diasIngresado


# Desarrollo del ejercicio
import numpy as np

habitaciones = np.zeros(10, int)
ruts = np.zeros(10, int)
nombresPersonas = ["","","","","","","","","",""]
idPersonas = np.zeros(10, int)
nombresMascotas = ["","","","","","","","","",""]
cantidadesDias = np.zeros(10, int)


def calcularPago(posicionHabitacion):
    valorDia = 15000
    diasPagar = cantidadesDias[posicionHabitacion]
    totalPagar = valorDia * diasPagar
    print("SU TOTAL A PAGAR ES:", totalPagar)
    habitaciones[posicionHabitacion] = 0
    ruts[posicionHabitacion] = 0
    nombresPersonas[posicionHabitacion] = ""
    idPersonas[posicionHabitacion] = 0
    nombresMascotas[posicionHabitacion] = ""
    cantidadesDias[posicionHabitacion] = 0

def hayHabitacionesDisponibles():
    if 0 in habitaciones :
        return True
    return False

def habitacionesDisponibles():
    habitacionesElegir = []
    for i in range(10):
        if habitaciones[i] == 0:
            habitacionesElegir.append(i + 1)
    return habitacionesElegir

def grabar(identificadorDisponible):
    rutPersona = validarRut()
    nombrePersona = validarNombre(3, 0)
    idPersona = identificadorDisponible
    identificadorDisponible = identificadorDisponible + 1
    nombreMascota = validarNombre(3, 1)
    cantidadDias = validarDias()

    if hayHabitacionesDisponibles():
        habitacionesElegir = habitacionesDisponibles()
        numeroHabitaciones = len(habitacionesElegir)
        for i in range(numeroHabitaciones):
            print(f"Opción {i+1}: Habitación {habitacionesElegir[i]}")
        habitacionElegida = validarOpcion(numeroHabitaciones)

        # Reservación
        habitacionElegida = habitacionElegida - 1
        habitaciones[habitacionElegida] = 1
        ruts[habitacionElegida] = rutPersona
        nombresPersonas[habitacionElegida] = nombrePersona
        idPersonas[habitacionElegida] = idPersona
        nombresMascotas[habitacionElegida] = nombreMascota
        cantidadesDias[habitacionElegida] = cantidadDias
        print("Reservación realizada con éxito")

    else:
        print("No quedan habitaciones disponibles")

def buscar():
    rutIngresado = validarRut()
    habitacion = -1
    for i in range(len(ruts)):
        if rutIngresado == ruts[i]:
            habitacion = i
    
    if habitacion != -1:
        print(f"La mascota de nombre {nombresMascotas[habitacion]} se encuentra en la habitación {habitacion + 1}")
    else:
        print("No se encontraron mascotas registradas con dicho rut")


def retirarse():
    rutIngresado = validarRut()
    habitacion = -1
    for i in range(len(ruts)):
        if rutIngresado == ruts[i]:
            habitacion = i
    
    if habitacion != -1:
        calcularPago(habitacion)
    else:
        print("No se encontraron mascotas registradas con dicho rut")

def salir():
    print("Programa finalizado")