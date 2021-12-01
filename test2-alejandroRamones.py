#Crear la función letraRepetida(letra, num) 
# que devuelve una cadena formada por letra repetida num veces
def letraRepetida(letra,num):
    return letra*num
letra=input("Introduce una letra: ")
num=int(input("Introduce un numero: "))
print(letraRepetida(letra,num))