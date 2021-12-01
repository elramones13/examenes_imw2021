# Crear la función media(lista), 
# a la que se le pasa una lista de números 
# y devuelve la media número de la lista
def media(lista):
    media1 = sum(lista) / len(lista)
    return media1
    
lista = [1, 67, 34, 77, 344, 24]
print("La media de los números es: ")
print (media(lista))
