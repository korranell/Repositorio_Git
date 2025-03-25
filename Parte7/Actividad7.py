#1- Define una clase Figura con un método de instancia area que devuelve el área de la figura. 
#a- Luego, crea clases hijas como Circulo y Rectangulo que hereden de Figura y proporcionen implementaciones diferentes del método area.

class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area (self):
        return self.base * self.altura

figura1 = Circulo(5)
figura2 = Rectangulo(5, 10)

print(figura1.area())
print(figura2.area())

#2- Crea una clase Calculadora con un método de clase llamado suma que acepte dos números comoargumentos y devuelva la suma de ellos. 
#a- Luego, utiliza este método para realizar algunas operaciones de suma.

class Calculadora:
    @classmethod
    def suma(cls, num1, num2):
        return num1 + num2

print(Calculadora.suma(7.5, 8))


#3- Crea una clase Empleado que tenga los siguientes atributos de instancia: nombre, apellido, edad, salario.
#a- Luego, crea una clase Gerente que herede de Empleado y tenga un atributo adicional departamento. 
#b- Define métodos de instancia para ambas clases, como mostrar_informacion para mostrar los detalles de un empleado y aumentar_salario para aumentar el salario de un empleado en un porcentaje dado. 
#c- Crea instancias de ambas clases y realiza algunas operaciones.

class Empleado:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Salario: {self.salario}")
    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100

class Gerente(Empleado):
    def __init__(self, nombre, apellido, edad, salario, departamento):
        super().__init__(nombre, apellido, edad, salario)
        self.departamento = departamento
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")

empleado1 = Empleado("Lautaro", "Morales", 23, 1600)
empleado2 = Gerente("Carlo", "Rossi", 45, 3000, "Compras")

empleado1.mostrar_informacion()
empleado1.aumentar_salario(25)
empleado1.mostrar_informacion()
empleado2.mostrar_informacion()

#4- Crea una clase Libro con atributos de instancia como titulo, autor, año_publicacion, y disponible (un valor booleano que indica si el libro está disponible o no). 
#a- Luego, crea una clase Biblioteca que tenga una lista de libros y métodos de instancia para prestar un libro, devolver un libro y mostrar todos los libros disponibles. 
#b- Utiliza atributos de clase para registrar la cantidad total de libros en la biblioteca.
#c- Crea instancias de ambas clases y realiza operaciones de préstamo y devolución de libros.

class Libro: 
    def __init__(self, titulo, autor, año_publicacion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = True

class Biblioteca():
    cantidad_libros = 0

    def __init__ (self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        Biblioteca.cantidad_libros += 1

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible == True:
                libro.disponible = False
                return f"El libro {titulo} ha sido prestado."
        return "El libro no se encuentra disponible."

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible == False:
                libro.disponible = True
                return f"El libro {titulo} ha sido devuelto."
            if libro.titulo == titulo and libro.disponible == True:
                return f"El libro {titulo} no ha sido prestado."
        return "El libro no se encuentra en la biblioteca."

    def mostrar_libros_disponibles(self):
        print("\nLibros disponibles:")
        for libro in self.libros:
            disponibilidad = "Disponible" if libro.disponible == True else "No disponible"
            print(f"Titulo: {libro.titulo} - Autor: {libro.autor} - Disponibilidad: {disponibilidad}")
        return "No hay libros en la biblioteca."


libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 1943, True)
libro2 = Libro("Harry Potter", "J.K. Rowling", 1997, True)
libro3 = Libro("El señor de los anillos", "J.R.R. Tolkien", 1954, True)
libro4 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, True)

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)

print(biblioteca.prestar_libro("El principito"))
print(biblioteca.devolver_libro("El principito"))
print(biblioteca.devolver_libro("El principito"))
biblioteca.mostrar_libros_disponibles()


#5- Crea una clase Producto con atributos de instancia como nombre, precio, cantidad_disponible y codigo_producto. 
#a- Luego, crea una clase CarritoCompras que permita a los clientes agregar productos, eliminar productos y calcular el total de la compra. 
#b- Utiliza un atributo de clase para rastrear la cantidad total de productos en el carrito de compras de todos los clientes. 
#c- Crea instancias de ambas clases y simula operaciones de compra.

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible, codigo_producto):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.codigo_producto = codigo_producto

class CarritoCompras:
    cantidad_total_productos = 0
    
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
        CarritoCompras.cantidad_total_productos += 1

    def eliminar_producto(self, codigo_producto):
        for producto in self.productos:
            if producto.codigo_producto == codigo_producto:
                self.productos.remove(producto)
                CarritoCompras.cantidad_total_productos -= 1
                return f"Producto {producto} eliminado."
        return f"Producto {producto} no encontrado."

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto[0].precio * producto[1]
        return f"El total de la compra es ${total}"


producto1 = Producto("Camisa", 500, 10, 1)
producto2 = Producto("Uranio enriquecido", 1000000, 1, 2)

carrito = CarritoCompras()
carrito.agregar_producto((producto1, 2))
carrito.agregar_producto((producto2, 1))
print(carrito.calcular_total())

