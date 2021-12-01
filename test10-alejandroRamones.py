#Crear la función enUnaLista(lista1, lista2) 
# a la que se le pasa dos listas de números y 
# devuelve una lista con los números que están en lista1 
# pero no están en lista2
def enUnaLista(lista1, lista2):
    lista3=[]
    for num in lista1:
        if(num not in lista2):
            lista3.append(num)
    return lista3

lista1 = [10, 60, 30, 40]
lista2 = [50, 60, 70, 40]
print(enUnaLista(lista1,lista2))
