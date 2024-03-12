""" def sumados(a, b):
    suma = a + b
    return suma
x = sumados(5, 6)
print(x) """

""" año = input('coloca un año: ')
def año_bisiesto(año):
    año % 4 == 0
    return f'el año {año} es bisiesto'
b = año_bisiesto
print(b) """

#Enronces podemos realizar una validacion
""" def resta(a=None, b=None):
	if a == None or b == None:
		print("Error, debes enviar dos valores a la funcion")
		return
	else:
		return a - b
resta()

x = resta(1, 5)
print(x) """
while True:

    try:
        enter = int(input('introduce un año:'))
        def año_bisiesto(enter):
           if enter % 100 != 0:
              return f'el año {enter} no es bisiesto'
           else:
              enter % 4 == 0
              return f'el año {enter} es bisiesto'
    except Exception:
        print('Ha ocurrido un error, debe colocar un número entero, no letras o palabras')
año_bisiesto(enter)
r = enter
print(r)
          