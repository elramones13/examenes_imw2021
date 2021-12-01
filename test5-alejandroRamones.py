#Crear la función comunes(lista1, lista2) 
# a la que se le pasa dos listas de números y 
# devuelve una lista con los números que tienen en común.
def comunes(lista1, lista2):
    iguales=[]
    #s1=set(lista1)
    #s2=set(lista2)
    #return list(s1 & s2)
    for num in lista1:
        if num in lista2:
            iguales.append(num)
    return list(set(iguales))
lista1=[1,5,99,44,676,32]
lista2=[5,88,5,676,90]
iguales=comunes(lista1, lista2)
print("Los comunes son: ", iguales)

