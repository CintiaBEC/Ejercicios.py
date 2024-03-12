
# Crear una variable que contenga el texto que ustedes quieran en formato byte , en lo posible extenso, y convertirlo a Unicode.

""" Primero voy a tomar un texto de interés y a convertirlo a byte, ya que no leemos en bytes y la consigna pide que 
tome un texto en bytes y lo convierta a unicode. Para ello uso .encode() """

# Copié en un archivo de Word un texto de interés, ahora lo convertiré a bytes. 
# Para poder trabajar con un archivo de word instalé docx2txt (abajo el enlace)
# https://www.desarrollo-web-br-bd.com/es/python/leer-el-archivo-.doc-con-python/823792610/#:~:text=Puede%20usar%20la%20biblioteca%20python,instalarlo%20ejecutando%3A%20pip%20install%20docx2txt%20.
# Una vez instalado docx2txt importo (siempre se importa al inicio), uso la sintaxis sugerida en la página web consultada.

from __future__ import unicode_literals
import docx2txt

texto = docx2txt.process('Bach.docx')

print(texto.encode())

print()


# A continuación lo que pensé pero no salió ni con bucle for, ni con open with, tampoco con docx2txt
""" Una vez impreso, lo copio tal cual desde la terminal en otro word y ahora lo convierto a unicode, usando docx2txt y creando una variable diferente
a la primera que utilcé, nada más que ahora lo vuelvo a formato unicode con el método .decode() """


byte = docx2txt.process('Bach_in_bytes.docx')

print(byte.decode) # Acá es donde no puedo introducir el método decode y todo se viene abajo, aún con formato .txt



    
