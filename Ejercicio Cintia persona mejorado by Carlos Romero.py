# Mi primera clase
""" 1.  Crear una clase para trabajar con una Persona. Agregarle 3 atributos de instancia, por lo menos 2 de clase, el constructor y dos métodos (uno con parámetros y otro sin parámetro).
2.  Luego instanciar a dos personas. """

# Para este ejercicio voy a simular que necesito personas de diferentes nacionalidades y que realicen deportes distintos para publicidad de ropa deportiva.
# Para ello necesito la altura, nacionalidad, sexo, el tipo de ctividad física de los potenciales modelos y los idiomas que manejan.

# CLASE: Persona

class Persona():

# Atributos de clase: aquí van atributos muy genéricos, comunes a todas las personas (por ejemplo, las inherentes a su biología)

    especie = "'Homo sapiens sapiens'"
    andar = "bipedo"

    #llamo mét. __init__ para crear objeto

    def __init__(self, nombre, apellido, edad, sexo, nacionalidad, altura):
        print(f'Modelo {nombre} {apellido}, {nacionalidad}')
   
    #Defino atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad
        self.altura = altura

    #Defino métodos, para mi caso, es la actividad física que realizan e idioma/as que manejan

    def tipo_actividad(self, *args):
        texto = ', '.join(args)
        print(f'Tipo de actividad/es que realiza: {texto}.')
        
    def idiomas(self, *args):
        texto = ', '.join(args)
        print(f'Manejo de idioma/as: {texto}.')

#Creo cada objeto, en este caso, cada persona que postula

persona_1 = Persona('Greta', 'Shnneichder', '28 años', 'sexo femenino', 'alemana', '1.78m')

print(persona_1.edad)
print(persona_1.sexo)
print(persona_1.altura)

""" Para llamar a las definiciones con argumentos *args, debo imprimir (print) el objeto seguido de punto y el nommbre de la función,
colocando entre paréntesis lo que dicha función pide, en este caso, uso *args para que si las personas practican más de un deporte
o, hablan más de un idioma, puedan cargarse a sus datos sin importar la cantidad"""

# USO DE LOS MÉTODOS CON *ARGS

persona_1.tipo_actividad('natación', 'esgrima')
persona_1.idiomas('alemán','francés')

print('-----------------------------------------------------------------------') # sólo agregué este print para que la terminal se vea ordenada y los objetos separados

persona_2 = Persona('Marco', 'Stepper', '25 años','sexo binario', 'argentino', '1.88m')

print(persona_2.edad)
print(persona_2.sexo)
print(persona_2.altura)

persona_2.tipo_actividad('basketball', 'tenis, hockey')
persona_2.idiomas('español', 'inglés', 'italiano')