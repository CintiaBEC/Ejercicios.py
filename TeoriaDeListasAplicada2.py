
'''# Concatenación de listas

letras = ['h', 'i', 'j', 'k', 'l']

números = [1, 2, 3, 74]

oración = ['había una vez']

# Concatenación de las 3 listas anteriores

# Uso signo '+' para concatenar

concatenación = letras + números + oración

print(concatenación)

# Uso 'comas' para concatenar

concatenación = letras, números, oración

print(concatenación)

# La diferencia de concatenar con signo +, o con coma, es cómo se ve el resultado final en la TERMINAL: con '+', todo va seguido y con comas; con ',' se distingue c/lista entre []'''

letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras[:3] = ['A', 'B', 'C', 'D']
print(letras)

