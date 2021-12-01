#Crear la función menorNum(lista), 
# a la que se le pasa una lista de números y 
# devuelve el menor número de la lista
def menorNum(lista):
    menor = min(lista)
    return menor
lista1 = [1,5,6,4,1,7,5,4]
print("El numero menor de la lista es:" , menorNum(lista1)) 