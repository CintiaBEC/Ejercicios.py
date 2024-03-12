""" Localiza el error en el siguiente bloque de código. Crea una función con la excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = 10/0 """

# oh nooo, dividió entre cero!!!!

from typing import final


c = 0

while True:
    try:
        enter = float(input('introduce un número "n" para realizar la divisón (100/n):'))
        dividir = 100
        print(f' La división de 100 por {enter} es {100/enter}')    
        if enter != 0:
                break
    except ZeroDivisionError:
        print('No se puede dividir por cero, vuelva a introducir otro número')
    except ValueError:
            print('Debe intriducir un número decimal o entero (no letras o palabras), si el número es decimal use punto en vez de coma, ejemplo: 2.5')  
    except Exception as e:
        print('Se produjo un error')
    finally:
        pass
