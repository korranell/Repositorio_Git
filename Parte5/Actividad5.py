#1- Gestión de tareas pendientes. Crea un programa que permita a un usuario llevar un registro de tareas pendientes. 
#El programa debe:
#a- Permitir al usuario agregar tareas.
#b- Marcar tareas como completadas agregándole un tilde o algo que identifique que se completó al principio de la tarea.
#c- Listar las tareas pendientes.

tareas = list()

print("\nBienvenido al sistema de gestion de tareas pendientes.")

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

def menu():
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
            break
        else:
            print("\nPor favor ingrese una opcion valida.")
            continue

#menu()

#2- Desarrolla un programa que permita a un usuario registrar información de contactos (nombre, número de teléfono y correo electrónico). 
#a- El programa debe almacenar estos contactos y permitir al usuario buscar contactos por nombre o número de teléfono.

base_de_datos = dict()

def registrar_contacto():
    global base_de_datos
    nombre = input("\nIngrese el nombre del contacto: ")
    numero_de_telefono = input("Ingrese el numero de telefono del contacto: ")
    correo_electronico = input("Ingrese el correo electronico del contacto: ")
    base_de_datos[nombre] = {"Numero de telefono": numero_de_telefono, "Correo electronico": correo_electronico}
    print("\nContacto registrado.")
    return

def buscar_contacto():
    criterio = input("Por favor ingrese una referencia: ")
    for nombre, info in base_de_datos.items():
        if criterio in nombre or criterio == info["Numero de telefono"]:
            print(f"\n{nombre}.")
            print(f"Telefono {info['Numero de telefono']}.")
            print(f"Correo electronico {info["Correo electronico"]}")
    return

def menu_contactos():
    while True:
        print("\n1- Registrar un contacto.")
        print("2- Buscar un contacto.")
        print("3- Salir del programa.")
        opcion = input("\nIngrese una opcion: ")
        if opcion == "1":
            registrar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            break
        elif opcion == "debug230430":
            print(base_de_datos)
        else: 
            print("\nPor favor ingrese una opcion valida.")
            continue

#menu_contactos()

#3- Crea un programa que permita a un usuario configurar la red de una computadora. 
#a- El programa debe aceptar argumentos clave para configurar la dirección IP, la máscara de subred y la puerta de enlace. 
#b- Luego, muestra la configuración de red completa

print("\nBienvenidos al programa de configuracion de red.")

def config_computadora(**kwargs: str) -> str:
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}.")
    print("\nConfiguracion realizada.")

while True:
    print("\n1- Configurar red.")
    print("2- Salir del programa.")
    opcion = input("\nIngrese una opcion: ")
    if opcion == "1":
        ip = input("Por favor ingresa la direccion IP: ")
        mascara = input("Por favor ingresa la mascara de subred: ")
        puerta = input("Por favor ingresa la puerta de enlace: ")
        config_computadora(direccion_ip = ip, mascara_subred = mascara, puerta_enlace = puerta)
    elif opcion == "2":
        break
    else:
        print("\nPor favor ingrese una opcion valida.")

#config_computadora()

#4- Crea un programa que permita calcular el promedio de un número variable de notas ingresadas por el usuario. 
#a- La función calcular_promedio puede recibir un número variable de notas.
#b- Luego, muestra el promedio de las notas ingresadas.

def calcular_promedio(*notas):
    total = sum(notas)
    if len(notas) > 0:
        promedio = total / len(notas)
        print(f"\nEl promedio es el siguiente {promedio}.")
    else:
        print("No se ingresaron notas.")

def ingresar_notas():
    while True:
        nota = float(input("Ingrese todas las notas (ingrese 0 para salir): "))
        if nota == 0:
            return
        notas.append(nota)

notas = []

def menu_promedio():
    while True:
        print("\n1- Ingresar las notas y calcular promedio.")
        print("2- Salir del programa.")
        opcion = input("\nIngrese una opcion: ")
        if opcion == "1":
            ingresar_notas(*notas)
            calcular_promedio(*notas)
        elif opcion == "2":
            break

menu_promedio()