
# Ejercicio Nº Impar

'''si un número es par, es divisible por dos, entoces el resto de la división sera igual a cero
para ello debemos utilizar el operador %', entonces:'''


while True:
    try:
        número_impar = int(input('Introduce un número impar:'))

        número_impar = número_impar % 2 != 0

        if número_impar != 0:
            print('¡Bien hecho!')
            break
        else:
           número_impar == 0 
           print('El número ingresado es par')

    except Exception as e:
        print('Ha ocurrido un error,', type(e).__name__,',vuelve a intentarlo')
    finally: 
        pass
print('¡Ha finalizado la prueba')
    

