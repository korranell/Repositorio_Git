#1- Escribe un programa que tome un número entero positivo ingresado por el usuario y muestre la tabla de multiplicar de ese número. 
#a- Repite la solicitud al usuario de ingresar un nuevo número hasta que ingrese un cero.

menu = True
while menu == True:
    numero = input("Ingrese un numero entero positivo: ")
    numero = int()
    if numero == 0:
        break
    if numero > 0: 
        for i in range (1,11):
            print(f"{numero} x {i} = {numero*i}")
    else:
        menu = False
        print("Gracias por usar el programa.")

#2- Escribe un programa que tome una lista de nombres ingresados por el usuario separados por un espacio y los liste mostrando su ubicacion.

nombre = input("Ingrese nombres separados por un espacio: ").split()
for indice, nombre in enumerate(nombre):
    print(f"Nombre {indice + 1}: {nombre}")


#3- Crea un programa que solicite al usuario ingresar una palabra. Luego, recorre la palabra y cuenta cuántas vocales contiene. 
#a- Al final, si no se encontraron vocales, muestra un mensaje comunicando que la palabra ingresada solo contiene consonantes.

palabra = input("Por favor ingresa una palabra: ")
vocales = "aeiouAEIOU"
contador_vocales = 0

for letra in palabra:
    if letra in vocales: 
        contador_vocales += 1

if contador_vocales == 0:
    print("La palabra no tiene vocales")
else: 
    print(f"La palabra tiene {contador_vocales} vocales")

#4- Escribe un programa que tome una lista de palabras ingresadas por el usuario. 
#a- Luego, que muestre cada palabra una por una. Si la palabra es "salir", finaliza el programa. Si la palabra es "omitir", se pasa a la siguiente iteración. 
#b- Al final, si ninguna palabra fue "salir", muestra un mensaje avisando la situación.

lista = input("Ingrese palabras separadas por coma: ").split(", ")
for palabra in lista:
    if palabra == "salir":
        break
    if palabra == "omitir":
        continue
    else: 
        print(palabra)
else: 
    print("No se encontro ninguna palabra.")

#5- Imagina que estás administrando un pequeño almacén y deseas realizar un seguimiento de los productos en tu inventario. 
#a- Escribe un programa que te permita ingresar el nombre y la cantidad de varios productos. 
#b- Utiliza un bucle para recorrer los productos y mostrar su nombre y cantidad. Al final, muestra el total de productos en el inventario.

inventario = {}
num_prod_actual = int(input("Ingresa la cantidad de productos a cargar: "))

for _ in range(num_prod_actual):
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    inventario[producto] = cantidad

print("\nInventario:") 
totalprod = 0

for producto, cantidad in inventario.items():
    print(f"{producto}: {cantidad}")
    totalprod += cantidad

print(f"\nTotal de productos en el inventario: {totalprod}.")

