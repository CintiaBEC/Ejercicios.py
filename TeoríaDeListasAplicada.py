
# Defino variables, creo listas, y con ellas armo una lista heterogénea llamada "todo"

a= 5
b = 'Hola'
lista1 = [1, 2, 3]
variable_1 = a
variable_2 = b
lista2 = ['¿Qué tal?', 'Soy Pepe'] 
todo = [lista1, variable_1, variable_2, lista2] # Esta es la lista llamada "todo"

print(todo)

print(todo[-3])  # Listas admiten index, como resultado voy  obtener el objeto que corresponde a índice -3, el objeto es 5.

# Listas admiten slicing (cortar)    -->    [inicio:fin:paso]

# 'todo' posee 4 objetos, 0 es el primer objeto, 3 es el cuarto objeto (uso index) que va a ser cortado (slicing), 1 representa la cantidad de objetos que quedan entre inicio y fin.
print(todo[0:3:1]) # Resultado: deja primer objeto, corta el cuarto.

# Voy a mantener el primer objeto (indice 0), voy a cortar el tercer objeto (indice 2), voy a conservar un objeto entre el primer y tercer objeto (indice 1).
print(todo[0:2:1])

# Equivalente a lo anterior (no necesito colocar cero).
print(todo[:2:1]) 

# Corta primer objeto (index 0), deja lo que está en el medio del primer  y el cuarto (index 3) objeto.
print(todo[1:3])

# Sólo corto primer objeto (index 0), conservo el resto de la lista. No es neceario definir fin ni paso.
print(todo[1:])

# Corto el último objeto, no necesito definir inicio ni fin.
print(todo[:3])
