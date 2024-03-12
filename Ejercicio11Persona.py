""" Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:
Un constructor, para sus atributos. Mencionar ¿Que tipo de atributos son?
mostrar(): Muestra los datos de la persona. 
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad. """

class Persona():   #clase Persona

#Atributos de clase
    reino = 'Animal'
    clase = 'mamifero'
    especie = 'Homo sapiens sapiens'
    andar = 'bípedo'
    
# Llamo mét. __init__ para crear objeto
    def __init__(self, nombre, edad, DNI):
        print(f'Nombre: {nombre}, Edad: {edad} años.')

# Defino atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

 # Defino métodos
    def mostrar(self):
        return print(f'Datos personales: {self.nombre}, {self.edad} años, {self.DNI}') 
    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True, 'es mayor de edad' 
        else:
            return False, 'es menor de edad'

#Creo cada objeto, en este caso, cada persona que postula (c/objeto es una instancia de clase)

persona_1 = Persona('Juan Peres', 33, 'DNI: 33654987')

print(persona_1.DNI)

# Uso los métodos creados

persona_1.mostrar()
print(persona_1.esMayorDeEdad())

# Ahora creo una persona2, para ver si entra al else, cuando es menor de edad
print('------------------------------------------------------') #sólo imprimo espacio para visualizar mejor

persona_2 = Persona('Aris Grenn', 14, 'DNI: 52546879')

print(persona_2.DNI)

# Uso los métodos creados

persona_2.mostrar()
print(persona_2.esMayorDeEdad())