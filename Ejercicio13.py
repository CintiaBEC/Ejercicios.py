
""" Crear un archivo.txt que dentro contenga un texto Unicode, abrirlo con Python, recorrerlo
 y transformarlo en un cadena de bytes. """
 
with open('mitexto.txt','r') as file:
    texto = file.read()

for line in file:
    
    print(line.encode)

    f.close()