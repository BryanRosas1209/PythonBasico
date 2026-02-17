# 1. Abstracción
# La abstracción es el proceso de ocultar los detalles internos de cómo funciona algo y mostrar solo lo necesario para usarlo.
# Ejemplo real: un cajero automático. El usuario solo ve opciones como retirar dinero o consultar saldo, pero no necesita saber cómo el sistema se conecta con el banco.
# En programación, esto ayuda a simplificar problemas complejos y enfocarse en lo esencial.

# Ejemplo de abstracción con un cajero automático
class CajeroAutomatico:
    def retirar_dinero(self, cantidad):
        print(f"Retirando {cantidad} pesos...")
# Clases vs. Objetos
# Clase: es el molde o plano que define atributos y métodos.

# Objeto: es una instancia concreta creada a partir de la clase.

# Ejemplo con Celular:

# Atributos: marca, modelo, batería.

# Métodos: llamar(), enviar_mensaje(), cargar_bateria().

# Clase Celular con atributos y métodos
class Celular:
    def __init__(self, marca, modelo, bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
    
    def llamar(self, numero):
        print(f"Llamando a {numero}...")
    
    def enviar_mensaje(self, numero, texto):
        print(f"Mensaje a {numero}: {texto}")
    
    def cargar_bateria(self):
        self.bateria = 100
        print("Batería cargada.")

# Creación de un objeto a partir de la clase
mi_celular = Celular("Samsung", "Galaxy S21", 80)
# 3. El Método Constructor __init__
# En Python, __init__ es un método especial que se ejecuta automáticamente al crear un objeto. Se le llama “mágico” porque no lo invocamos directamente, pero siempre se ejecuta. Su función principal es inicializar atributos.


# Ejemplo del método constructor __init__
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# 4. El parámetro self
# self representa al propio objeto que está usando el método. Es obligatorio porque permite acceder a los atributos y métodos de esa instancia.
# Sin self, el método no sabría a qué objeto pertenece la acción.

# 5 Encapsulamiento y Niveles de Acceso
# El encapsulamiento protege los datos internos de una clase. En Python se logra con guiones bajos:

# _atributo: indica que es “interno” (convención, no bloquea el acceso).

# __atributo: activa un mecanismo llamado name mangling, que dificulta el acceso directo desde fuera.

# Ejemplo de encapsulamiento con atributos privados
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # privado
    
    def mostrar_saldo(self):
        return self.__saldo
# Herencia: Reutilización de Código
# La herencia permite que una clase hija use atributos y métodos de una clase padre.

# Ejemplo de herencia con clases Animal, Perro y Gato
class Animal:
    def hablar(self):
        print("Sonido genérico")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")
# Ventaja: evita repetir código y facilita la organización.

# Polimorfismo
# El polimorfismo significa que diferentes clases pueden tener métodos con el mismo nombre, pero cada uno se comporta distinto.

# Ejemplo de polimorfismo con Cuadrado y Círculo
class Cuadrado:
    def calcular_area(self, lado):
        return lado * lado

class Circulo:
    def calcular_area(self, radio):
        return 3.14 * radio * radio
# Composición vs. Herencia
# La composición ocurre cuando una clase contiene objetos de otra clase en lugar de heredar de ella.
# Ejemplo: un Coche que tiene un Motor, pero no hereda de él.

# Ejemplo de composición: un coche que contiene un motor
class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self):
        self.motor = Motor()
    
    def arrancar(self):
        self.motor.encender()
        print("Coche en marcha")
# Estado de un Objeto
# El estado de un objeto es el conjunto de valores que tienen sus atributos en un momento dado. Los métodos pueden cambiar ese estado.

# Ejemplo del estado de un objeto con una lámpara
class Lampara:
    def __init__(self):
        self.encendida = False
    
    def prender(self):
        self.encendida = True
    
    def apagar(self):
        self.encendida = False
# Ventaja del Paradigma Orientado a Objetos
# Reutilización de código mediante herencia y polimorfismo.

# Organización y claridad: el código se estructura en clases y objetos.

# Mantenimiento más sencillo: los cambios se hacen en una clase y afectan a todos los objetos derivados.