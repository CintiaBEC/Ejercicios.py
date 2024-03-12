
# Voy a generar una lista y a trabajar sobre la misma
lista1 = ["hola", 1, 2, 3, "probando"]
print(lista1)
# Voy a generar una tupla e incluir a lista1 como elemento de la misma
tupla1 = (lista1, "qué tal gente", "¡Welcome!")
print(tupla1)
# Aplicaré método insert en la posición 1 de la lista1
lista1.insert(1, "¡me escuchan?")
print(lista1)
# Ahora, imprimiré la tupla para verificar que se agregó la modificación en lista1
print(tupla1)
