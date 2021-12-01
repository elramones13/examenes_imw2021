#Crear la función menorMayor(tupla), 
# a la que se le pasa una tupla y devuelve 
# una lista con dos valores, 
# el menor y el mayor de la tupla original.
def menorMayor(tupla):
    mayor=max(tupla)
    menor=min(tupla)
    return mayor,menor
tupla=(10,5,140,200,2,1)
print (menorMayor(tupla))
