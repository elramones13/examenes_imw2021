#Crear la función listaImpares(lista) 
# a la que se le pasa una lista de números y 
# devuelve otra lista sólo con los números impares de la 
# lista original.
def listaImpares(lista):
    lista1=[]
    for num in lista:
        if num % 2 != 0:
            lista1.append(num)
    return lista1
lista=[40,15,6,55,9,2,1]
impares=listaImpares(lista)
print("Los números impares de la lista son: " + str(impares))
