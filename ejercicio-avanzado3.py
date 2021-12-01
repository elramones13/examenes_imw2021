#Crear la función contarFichero(fichero, palabra)
#  a la que se le pasa el nombre de un fichero de texto (nombre.txt) 
# y devuelve cuantas veces aparece palabra dentro de ese 
# fichero de texto. Uy, que no habíamos visto ficheros, 
# pues ala a buscar como se usan, aquí por ejemplo.
def contarFichero(fichero,palabra):
    repetidas = 0
    lines = fichero.readlines()
    for line in lines:
        palabras=line.split()
        for p in palabras:
            if p==palabra:
                repetidas=repetidas+1
    return palabra, repetidas
palabra = "adios"
fichero = open("nombre.txt", "rt")
print (contarFichero(fichero, palabra))

#f = open(fichero)
#texto = f.read()
#veces=texto.upper().count(palabra)

