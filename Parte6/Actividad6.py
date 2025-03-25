#1- Desarrolla un programa que permita al usuario buscar información sobre ciudades. Tendrás un diccionario llamado ciudades_info que contiene información sobre algunas ciudades, como su país, población y puntos de interés. 
#a- El programa debe permitir al usuario ingresar el nombre de una ciudad y mostrar la información correspondiente. 
#b-El programa debe poder manejar el caso en el que la ciudad no existe en el diccionario y mostrando un mensaje avisando del error.

ciudades_info = {'Paris': {'Pais': 'Francia','Poblacion': 2187526, 'Puntos_de_Interes': ['Torre Eiffel','Louvre', 'Catedral de Notre-Dame']},
'Nueva York': {'Pais': 'Estados Unidos','Poblacion': 8398748,'Puntos_de_Interes': ['Estatua de la Libertad', 'Central Park', 'Times Square']},
'Tokio': {'Pais': 'Japón','Poblacion': 13929286,'Puntos_de_Interes': ['Torre de Tokio','Templo Senso-ji', 'Palacio Imperial']}}

ciudad = input("Por favor ingrese el nombre de una ciudad a buscar: ")

try:
    info = ciudades_info[ciudad]
    print(f"\n{ciudad}.")
    print(f"Pais: {info['Pais']}.")
    print(f"Poblacion: {info['Poblacion']}.")
    print(f"Puntos de Interes: {info['Puntos_de_Interes']}")
    print("\n")
except KeyError:
    print(f"Error: La ciudad '{ciudad}' no se encuentra en la base de datos.")


#2- Escribe un programa que permita al usuario ingresar su edad. 
#a- El programa debe validar si la edad ingresada está dentro del rango de 18 a 65 años, y mostrar un mensaje correspondiente. 
#b- Utiliza un bloque try-except con múltiples bloques except para manejar posibles errores relacionados con la entrada del usuario, como una entrada no numérica o una edad fuera del rango válido.
#Tip: puedes usar la funcionalidad 'raise' para que se genere una excepción.

try:
    edad = input("Por favor ingrese su edad: ")
    edad = int(edad)
    if edad < 18 or edad > 65:
        raise ValueError("Edad fuera del rango permitido")
    if edad < 0: 
        raise ValueError("Edad no puede ser negativa")
    print(f"Edad {edad} dentro del rango permitido.")
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error: Entrada no válida ({e})")

#3- Escribe un programa que permita al usuario ingresar el precio de un producto y un código de descuento. 
#a- El programa debe validar si el precio es un número positivo y si el código de descuento es válido. 
#b- Los errores posibles incluyen entradas no numéricas, números negativos y códigos de descuento no válidos

descuentos_validos = ["DESC10", "DESC20", "DESC30"]

try: 
    precio = input("Ingrese el precio del producto: ")
    codigo = input("Ingrese el codigo de descuento: ")
    precio = float(precio)
    if precio < 0: 
        raise ValueError("El precio no puede ser negativo.")
    if codigo not in descuentos_validos:
        raise ValueError("Codigo de descuento no valido.")
    else: 
        if codigo == "DESC10":
            print(f"El precio final es: {float(precio) * 0.9}")
        elif codigo == "DESC20":
            print(f"El precio final es: {float(precio) * 0.8}")
        elif codigo == "DESC30": 
            print(f"El precio final es: {float(precio) * 0.7}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Error: Entrada no válida ({e})")
except TypeError as te:
    print(f"Error: Entrada no válida ({te})")