'''Realizar una función llamada año_bisiesto:

Recibirá un año por parámetro
Imprimirá “El año año es bisiesto” si el año es bisiesto
Imprimirá “El año año no es bisiesto” si el año no es bisiesto
Si se ingresa algo que no sea número debe indicar que se ingrese un número.

Información a tener en cuenta al realizar el ejercicio:
Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. 
Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.'''

# Resolución

#PRIMERO LO HICE CON INPUT Y WHILE 

""" while True:

    try:
        enter = int(input('introduce un año:'))
        if enter % 4 == 0:
           print('el año ingresado es bisiesto')
           break
        else:
            enter % 100 != 0
            print('el año ingresado no es bisiesto')    
    except Exception:
        print('Ha ocurrido un error, debe colocar un numero entero, no letras o palabras')
    finally: 
        pass
print('fin de consulta')
 """
#AQUÍ INTENTÉ SIN EXITO DEFINIR LA FUNCIÓN DENTRO DEL BUCLE WHILE, PERO NO LOGRO ENTENDER LA DECLARACIÓN Y LLAMADA DE UNA FUNCIÓN CUANDO POSEEN ARGUMENTOS
           
while True:

    try:
        enter = int(input('introduce un año:'))
        def año_bisiesto(enter):
            return enter
        if enter % 4 == 0:
            print(f'el año {enter} es bisiesto')
            break
        else:
            enter % 100 != 0
            print(f'el año {enter} no es bisiesto')    
    except Exception:
        print('Ha ocurrido un error, debe colocar un numero entero, no letras o palabras')
    finally:
            pass
año_bisiesto(enter)
print(año_bisiesto(2004))


