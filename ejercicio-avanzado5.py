#Usando la librería requests (que ya viene con python de fábrica) 
# crear la función contarPalabras(url,palabra), 
# a la que le pasamos una URL 
# y nos devuelve cuantas veces aparece una 
# palabra en la web de la url pasada.
import requests
def contarPalabras(url,palabra):
    respuesta=requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.text.count(palabra)
    else:
        return "Error"
url = "https://www.windbluesports.com"
palabra = "buceo"
resultado=contarPalabras(url,palabra)
print("La palabra", "\033[1m" + palabra.upper()+"\033[0m" ,"se ha repetido",  resultado , "veces en la web:",  "\033[1m"+url.upper()  )
