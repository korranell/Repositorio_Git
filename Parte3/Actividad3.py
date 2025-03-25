#1. Crea un programa que solicite dos números enteros al usuario y determine si ambos son números pares.

numero_1 = input("Ingrese el primer número: ")
numero_2 = input("Ingrese el segundo número: ")

if numero_1.isdigit() and numero_2.isdigit():
    if numero_1 % 2 == 0 and numero_2 % 2 == 0: 
        print("Ambos numeros son pares.")
    if numero_1 % 2 == 0 and numero_2 % 2 == 1: 
        print("El numero 1 es par y el numero 2 es impar.")
    if numero_1 % 2 == 1 and numero_2 % 2 == 0: 
        print("El numero 2 es par y el numero 1 es impar.")
    if numero_1 % 2 == 1 and numero_2 % 2 == 1:
        print("Ambos numeros son impares.")
else: 
    print("Por favor, ingrese dos números enteros. ")

#2- Escribe un programa que tome un número entero ingresado por el usuario y determine si es un número par, divisible por 3 y 5 al mismo tiempo, o ninguno de los anteriores.

numero = input("Ingrese un número entero: ")
if numero.isdigit(): 
    numero = int(numero)
    if numero % 2 == 0 and numero % 3 == 0 and numero % 5 == 0:
        print("El número es par y divisible por 3 y 5.")
    elif numero % 2 == 0:
        print("El número es par")
    elif numero % 3 == 0 and numero % 5 == 0:
        print("El número es divisible por 3 y 5.")
    else:
        print("El número no es par ni divisible por 3 y 5.")
else: 
    print("Por favor, ingrese un número entero.")

#3- Crea un programa que solicite un número entero al usuario y determine si es un número negativo, positivo o igual a cero. 
#a- En caso de ser positivo, verifica si es par o impar.

nombre = input("Ingrese su nombre: ")
numero = input(f"Por favor, {nombre}, ingrese un número entero: ")
if numero.isdigit():
    numero = int(numero)
    if numero < 0: 
        print("El numero es negativo.")
    if numero == 0:
        print("El numero es igual a cero.")
    if numero > 0: 
        if numero % 2 == 0: 
            print("El numero es positivo y par.")
        else: 
            print("El numero es negativo e impar.")
else:
    print("Por favor, ingrese un número entero.")

#4- Escribe un programa que tome un número entero ingresado por el usuario y muestre "Es positivo" si el número es mayor que cero, de lo contrario, muestra "No es positivo".

numero = input("Ingrese un número entero: ")
if numero.isdigit():
    numero = int(numero)
    if numero > 0:
        print("Es positivo.")
    else: 
        print("No es positivo.")
else: 
    print("Por favor, ingrese un número entero.")