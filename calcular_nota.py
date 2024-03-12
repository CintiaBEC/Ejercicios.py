
'''"Calcular nota'''

# Creacion variables 

# transformo a flotante el estilo de datos que coloco en imput, dado que se calcularán promedios.
# de forma predeterminada imput convierte la entrada en string, por ello agregamos previamente float para decirle al programa el tipo de objeto que tendrá

nota_1 = float(input("introduce nota primer exámen:"))         
nota_2 = float(input("introduce nota segundo exámen:"))        

promedio = (nota_1 + nota_2) / 2 

# coloco 'f-string' para invocar datos en print para que el programa arroje la leyenda 'el promedio final del estudiantes es:' seguida del promedio expresado como un número decimal

print(f'el promedio final del estudiantes es: {promedio}')

# qué ocurriría si escribo lo mismo, pero modifico float por int? VEAMOS

nota_1 = int(input("introduce nota primer exámen:"))         # si deseo introducir notas con decimales no va a arrojar el resultado porque indique que la entrada debían ser enteros
nota_2 = int(input("introduce nota segundo exámen:"))        # si por el contrario las notas que coloco son enteros, el programa corre sin problemas

promedio = (nota_1 + nota_2) / 2 

# si no defino en print el tipo de dato que va a arrojar 'promedio', lo entrega como float. Pero, si le digo al programa que lo entregue como int lo redondea a entero.

print(f'el promedio final del estudiantes es: {promedio}')

print(f'el promedio final del estudiantes es: {int(promedio)}')
