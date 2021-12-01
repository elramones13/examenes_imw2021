#Crear la función multiplosTres(lista) 
# a la que se le pasa una lista de números 
# y devuelve otra lista sólo con los números 
# múltiplos de 3 de la lista original.
def multiplosTres(lista):
    lista3 = []
    for n in lista:
        if n%3 == 0:
            lista3.append(n)
    return lista3

lista = [1, 4, 3, 324, 654,20,477,6689]
print(multiplosTres(lista))
