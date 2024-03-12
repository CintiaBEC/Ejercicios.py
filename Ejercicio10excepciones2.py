
""" Realizar una función llamada par_o_impar:
Recibirá un número por parámetro.
Imprimirá Par si el número es par
Imprimirá Impar si el número es impar
Si se ingresa algo que no sea número debe indicar que se ingrese un número. """

# Creo una función llamada par_o_impar, utilizando "def

def par_o_impar(número):     # defino un parámetro y lo denomino 'número'
    
    try:    
        if número % 2 == 0:
            print(f'el número {número} es par')
            pass
        else:
            número % 2 != 0
            print(f'el número {número} es impar')
    except Exception as e:
            print('debes introducir un número entero, no palabras, símbolos o letras')


par_o_impar('6')
par_o_impar(6)
par_o_impar(3)

