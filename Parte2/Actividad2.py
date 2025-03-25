#1- Crea un programa que solicite al usuario ingresar nombres separados por comas. 
#a- Luego, crea un conjunto con los nombres ingresados y muestra por pantalla la cantidad de nombres únicos en el conjunto.

nombres = input("Ingrese nombres separados por comas: ")
nombres = nombres.split(",")
nombres = set(nombres)
print(f"Los nombres son: {nombres}.")

#2- Crea un programa que simule un inventario de productos en una tienda. Inicia con un diccionario que contenga algunos productos y sus cantidades. 
#a- Luego, permite al usuario agregar un nuevo producto con su cantidad y actualizar la cantidad de un producto existente. Muestra el inventario actualizado.

inventario = dict(Manzanas = 50, Bananas = 30, Peras = 40)
nuevo_producto = input("Ingrese el nombre del producto: ")
nuevo_cantidad = int(input("Ingrese la cantidad del producto: "))
inventario.update({nuevo_producto: nuevo_cantidad})
print(f"El actual inventario es el siguiente: {inventario}.")

mensaje_actualizacion = input("¿Desea actualizar la cantidad de un producto? (y/n): ")
if mensaje_actualizacion == "y":
    producto = input("Ingrese el nombre del producto a actualizar: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    inventario.update({producto: cantidad})
    print(f"El actual inventario es el siguiente: {inventario}.")

#3- Crea un programa que tome una oración ingresada por el usuario y realice las siguientes operaciones: 
#a- Convierte la oración a mayúsculas
#b- Cuenta cuántas veces aparece la palabra "python"
#c- Muestra la oración sin espacios en blanco al inicio y al final.

oracion = input("Ingrese una oración: ")
oracion_en_mayusculas = oracion.upper()
oracion_cant_python = oracion.count("Python" or "python")
oracion_sin_espacios = oracion.strip()
print(f"La oracion en mayusculas es la siguiente: {oracion_en_mayusculas}.")
print(f"La cantidad de veces que se ha dicho Python es la siguiente: {oracion_cant_python}.")
print(f"La oracion sin espacios al principio o al final es: {oracion_sin_espacios}.")

#4- Crea dos conjuntos con números ingresados por el usuario y separados por coma. 
#a- Luego, muestra cuáles elementos tienen en común los conjuntos y crea un nuevo conjunto que contenga la unión de ambos.

conjunto_1 = set(input("Ingrese números separados por coma: ").split(","))
conjunto_2 = set(input("Ingrese números separados por coma: ").split(","))
print(f"Los elementos en común son: {conjunto_1.intersection(conjunto_2)}.")
conjunto_3 = conjunto_1.union(conjunto_2)
print(f"El conjunto combiando es: {conjunto_3}.")
mensaje_orden = input("¿Desea ordenar el conjunto combinado? (y/n): ")
if mensaje_orden == "y":
    conjunto_3 = sorted(conjunto_3)
    print(f"El conjunto combinado ordenado es: {conjunto_3}.")