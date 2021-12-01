#Crear la función mayorMenor(tupla1, tupla2), 
# a la que se le pasa dos tuplas 
# y devuelve una lista con dos valores, 
# el menor y el mayor de las dos tuplas. 
# No el mayor y menor de cada tupla, sino el mayor y 
# menor de los números que hay en las dos tuplas.
def mayorMenor(tupla1, tupla2):
    tupla3=tupla1+tupla2
    return [max(tupla3), min(tupla3)]

tupla1 = (4, 6, 123, 5646)
tupla2 = (1, 754, 865)
print("Los numeros mayores y menores de las dos tuplas son:")
print(mayorMenor(tupla1,tupla2))
