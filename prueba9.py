def palabrasComunes(frase1, frase2):
    iguales = []
    for num in frase1:
        if num in frase2:
            iguales.append(num)
    return list(set(iguales))


lista1 = ["hola","que","tal"]
lista2 = ["hola"]
iguales = palabrasComunes(lista1, lista2)
print("Los comunes son: ", iguales)
