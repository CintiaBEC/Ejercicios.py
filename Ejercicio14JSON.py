
# Convertir una lista de cadenas a formato JSON.
""" Pista: a la hora de crear una lista los contenidos dentro de la misma se muestran con una comilla simple ‘ ‘ pero cuando está convertida a json
 la lista se muestra con comillas dobles “ “ """

 # Para trabajar con json debo importar la su librería

import json

# Al igual que en diccionarios, json presenta estructura propiedad (llave) = valor 

# Creo un diccionario que contiene cadenas con datos diversos, para luego convertirlos a json

lista = {
   
    'Marca' : 'adidas',
    'Talle' : '35, 36, 37, 38, 39, 40',
    'Tipo' : 'unisex',
    'Colores' : 'blanco, azul, rosa, marrón, negro',
    'Cordones' : 'estampados con motivos en gris',
    'Disponibles' : '20 pares',
    'Disponibilidad x/talle' : {
        't35': 2,
        't36':3 ,
        't37': 4,
        't38': 3,
        't39':4,
        't40': 4
        },
    'Tienda web' : 'todos los modelos en vista'

}

print(type(lista))

with open("ejercicio14_json.json", 'w') as file:
    json.dump(lista, file, indent=3)
