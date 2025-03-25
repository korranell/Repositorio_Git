#1- Escribe un programa en Python que permita a un usuario registrar sus gastos diarios en un archivo de texto llamado "gastos.txt". 
#a- El programa debe permitir al usuario ingresar la descripción del gasto y la cantidad gastada.
#b- Luego, debe guardar estos datos en el archivo en el siguiente formato: "Fecha: {fecha} - Descripción: {descripción} - Cantidad: {cantidad}"
#Donde fecha es la fecha actual y descripción y cantidad son los datos ingresados por el usuario.


from datetime import datetime

def fecha_actual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def registrar_gasto():
    with open("gastos.txt", "a") as archivo:
        descripcion = input("Ingrese la descripción del gasto: ")
        cantidad = input("Ingrese la cantidad gastada: ")
        archivo.write(f"Fecha: {fecha_actual()} - Descripción: {descripcion} - Cantidad: ${cantidad}\n")
        print("Gasto registrado con éxito.")

def mostrar_gastos():
    try:
        with open("gastos.txt", "r") as archivo:
            gastos = archivo.read()
            print("\n--- Gastos Registrados ---")
            print(gastos)
    except FileNotFoundError:
        print("\nNo se han registrado gastos aún.")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar gasto")
        print("2. Mostrar gastos")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_gastos()
        elif opcion == "3":
            print("\n¡Gracias por usar el programa! Hasta luego 👋")
            return
        else: 
            return

#menu()

#2- Basándonos en el ejercicio 1 de funciones, edita el código para que el programa guarde el listado de tareas en un json al terminar la ejecución del programa y lo recupere al iniciarse el mismo.
#Notas actividad 2: (Aclaraciones)
#Ten en cuenta que el modo read del open genera un error al querer abrir un archivo que no existe.
#Y, a diferencia del read en los txt, el json.load también genera un error si el archivo no tiene nada.

import json 

try: 
    tareas = json.load(open("tareas.json", "r"))
except FileNotFoundError:
    tareas = []

#print("\nBienvenido al sistema de gestion de tareas pendientes.")

def agregar_tareas():
    tarea = input("Por favor ingrese su tarea a realizar: ")
    tareas.append(tarea)
    print("\nTarea agregada.")
    return

def tarea_completada():
    mostrar_tareas()
    indice = int(input(f"\nIngrese el numero de la tarea a completada: "))
    if 1 <= indice <= len(tareas):
        tareas[indice - 1] = tareas[indice - 1] + " ✓"
    print("\nTarea marcada como completada.")
    return

def mostrar_tareas():
    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea}")
    return

def menu1():
    while True:
        print("\n1- Agregar una nueva tarea.")
        print("2- Marcar una tarea como completada.")
        print("3- Mostrar el estado de todas las tareas")
        print("4- Salir del programa.")
        opcion = input(f"\nPor favor ingrese una opcion (1-4): ")
        if opcion == "1":
            agregar_tareas()
        elif opcion == "2": 
            tarea_completada()
        elif opcion == "3": 
            mostrar_tareas()
        elif opcion == "4":
            print("\nHasta luego.")
            with open("tareas.json", "w") as archivo:
                json.dump(tareas, archivo, indent=4)
                return
        else:
            print("\nPor favor ingrese una opcion valida.")
            continue

#menu1()

#3- Escribe un programa que permita a un profesor registrar las calificaciones de sus estudiantes en un archivo json llamado "calificaciones.json".
#a- El programa debe permitir al profesor ingresar nombres de estudiantes y sus calificaciones. 
#b- Luego, debe guardar estos datos en el archivo cuando termine el programa para persistir estos datos para futuras ejecuciones del programa. 
#c- Utilizar los nombres de los alumnos como claves y las notas como valores.

import json

try:
    with open("calificaciones.json", "r") as archivo:
        calificaciones = json.load(archivo)

except FileNotFoundError:
    calificaciones = {}

def agregar_calificaciones():
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    calificaciones[nombre] = calificacion

def mostrar_calificaciones():
    for nombre, calificacion in calificaciones.items():
        print(f"{nombre}: {calificacion}")

def menu2():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar calificaciones")
        print("2. Mostrar calificaciones")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            agregar_calificaciones()
        elif opcion == "2":
            mostrar_calificaciones()
        elif opcion == "3":
            with open("calificaciones.json", "w") as archivo:
                json.dump(calificaciones, archivo, indent=4)
            print("\n¡Gracias por usar el programa! Hasta luego 👋")
            return
        else:
            break

menu2()