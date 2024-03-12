
""" EJERCICIO 15 """

# Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla un diagrama de líneas con la evolución de las ventas.

# Importamos el modulo pyplot con el alias plt

import matplotlib.pyplot as plt

""" ENLACES CONSULTADOS """
#https://colab.research.google.com/github/asalber/aprendeconalf/blob/master/content/es/docencia/python/ejercicios/soluciones/matplotlib/ejercicio1.ipynb#scrollTo=Mmv7dhV70PUE
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=21&codigo=21&inicio=15
#https://www.youtube.com/watch?v=ZlLUSI4UipI
#https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D
#https://matplotlib.org/stable/api/markers_api.html


# Creamos dos listas vacías para cada dato que el usuario introducirá

años = []

ventas = []

# Sólo le pediré 3 años y sus ventas promedio respectivas, para ello usaré loop for
# La idea es que asigne a cada año el promedio de ventas

for num in range(3):

    año = input('ingrese año correspondiente a venta:')

    años.append(año)

    venta = input('ingrese valor promedio de venta de este año:')
    
    ventas.append([venta])

for i in range(3):
    print(años[i], ventas[i][0])

# Imprimo las listas para que me de dos listas que se correlacionen elemento a elemento y la copio desde terminal

print(años, ventas)

#['2019', '2020', '2021'] [['5689'], ['6874'], ['9524']]

# Ahora con las listas armo el diagrama de lineas, siendo la primer lista la que corresponderá a eje 'x' y la segunda a eje 'y':

#Llamaremos al método Line Plot para este gráfico y lo personalizaré o moriré en el intento

años = ['2019', '2020', '2021']

ventas = ['5689','6874','9524']

plt.plot(años, ventas, marker="h", linestyle="-", color="turquoise") 

#TÍtulo del gráfico
plt.title("Promedio de ventas 2019-2021")

#Nombramos los ejes
plt.xlabel("Años")
plt.ylabel("Promeio de ventas")

plt.figure(figsize=(1, 1000))
plt.show()