cadena = 'Python' #indexación diapo23

print(cadena[3]) 
print(len(cadena))
#Slicin es recortar, entre corchetes
print(cadena[0:4:1])
print(cadena[0:5:2]) #puedo obviar el cero porque Py lo sabe
#reasignar valores a los string
print(cadena[1] = 'y')
print(cadena)
print(cadena = cadena[:1] + 'y' + cadena[2:]) #p + y + thon