# Crear la función organizar(cantidad) 
# a la que se le pasa cantidad, 
# que es un entero. 
# La función generará cantidad de números aleatorios entre 0 y 100, 
# y a continuación  devolverá una diccionario con 10 elementos con índices 
# del 0 al 9, de tal manera que si el diccionario que devuelve 
# lo guardamos en la variable d, d[0]  de contiene los números 
# generados aleatoriamente que acaban en 0, d[1] contiene los números 
# generados aleatoriamente acabados en 1, 
# y así sucesivamente hasta d[9].
import random
def organizar(cantidad):
    while (cantidad >= 0):
        num = str(random.randint(0, 100))
        d[int(num[len(num) - 1])].append(int(num))
        cantidad -= 1
    return(d)
d = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
print(organizar(10))
