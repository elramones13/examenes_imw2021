# Crear la función contarPalabra(texto), 
# a la que se le pasa un texto y 
# devuelve una lista de listas de dos elementos.
# De las listas de dos elementos, el primer elemento 
# será una palabra y el segundo la cantidad de veces que 
# aparece en el texto. En otras palabras la función devuelve 
# cuantas veces aparece cada palabra en texto.
def contarPalabra(texto):
    lista1 = []
    lista2 = []
    lista3 = []
    for palabra in texto.split():
        lista1.append(palabra)
        lista2.append(texto.count(palabra))
        lista3 = zip(lista1, lista2)
    return list(set(lista3))
texto = ("hola que tal tal")
print(contarPalabra(texto))    
