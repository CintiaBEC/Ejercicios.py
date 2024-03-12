
# Ejercicio 6- 'números'

# Sin manejo de errores

""" n = 0

while True:
    enter = int(input('coloca un número entero:'))
    if enter == 0:
        break
    print(f'ingresó el número {enter}')
print('Finalizado') """

# Con manejo de errores

n = 0

while True:
    try:
        enter = int(input('coloca un número entero:'))
        enter = int(enter)
        print(f'ingresó el número {enter}')    
        if enter == 0:
                break
    except ValueError:
            print('Debe intriducir un número entero.')  
print('Finalizado')
 


