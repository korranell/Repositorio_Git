#1- Escribe un programa que solicite al usuario dos números enteros. Luego, muestra por pantalla la suma, resta, multiplicación y división de esos dos números.

numero_1 = int(input("Ingrese un numero entero: "))
numero_2 = int(input("Ingrese otro numero entero: "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

print(f"La suma de los dos numeros es: {suma}.")
print(f"La resta de los dos numeros es: {resta}.")
print(f"La multiplicacion de los dos numeros es: {multiplicacion}.")
print(f"La division de los dos numeros es: {division}.")

#2- Crea un programa que tome una cadena de texto como entrada del usuario. 
#a- Luego, muestra por pantalla los primeros tres caracteres de la cadena, seguidos por los tres últimos caracteres. 
#b- Además, concatena ambos subconjuntos y muestra el resultado

cadena = input("Ingrese una cadena de texto: ")
primeros_tres = cadena[:3]
ultimos_tres = cadena[-3:]
concatenacion = primeros_tres + ultimos_tres

print(f"Los primeros tres caracteres de la cadena son: {primeros_tres}.")
print(f"Los ultimos tres caracteres de la cadena son: {ultimos_tres}.")
print(f"La concatenacion de ambos subconjuntos es: {concatenacion}.")

#3- Crea un programa que inicie con una lista de números enteros. 
#a- Luego, solicita al usuario un número entero y un índice para reemplazar un elemento en la lista por el nuevo número ingresado en el índice ingresado. 
#b- Imprime la lista resultante.

lista = [1, 2, 3, 4, 5]
numero = int(input("Ingrese un numero entero: "))
indice = int(input("Ingrese un indice para reemplazar un elemento en la lista: "))
lista[indice] = numero
print(f"La lista resultante es: {lista}.")

#4- Crea un programa que, teniendo en cuenta la siguiente tupla, muestre el valor del segundo elemento de la misma. 
#a- Además, debe mostrar cuántas veces se repite este valor y cuál es el índice del valor repetido.

palabras_tupla = ("manzana", "pera", "uva", "naranja", "sandía", "manzana", "plátano", "kiwi", "pera", "fresa", "mango", "uva", "cereza", "manzana", "durazno")

segundo_elemento = palabras_tupla[1]
repeticiones = palabras_tupla.count(segundo_elemento)
indice = palabras_tupla.index(segundo_elemento)

print(f"El segundo elemento de la tupla es: {segundo_elemento}.")
print(f"El segundo elemento se repite {repeticiones} veces.")
print(f"El indice del segundo elemento repetido es: {indice}.")