# Utilizando pip3 instalar la librería arrow, 
# que sirve para trabajar con fechas. 
# Crear la función tiempo(day, moth, year) 
# a la que se le pasa un dia, mes y año, 
# y a devuelve con texto natural cuanto  tiempo ha pasado 
# desde esa fecha, o cuanto falta si es una fecha del futuro. 
# La librería arrow hace lo que estoy pidiendo. 
# P.e. si paso tiempo(1,9,2019) la función devolverá: 
# hace 3 días
import arrow
hoy = arrow.get(2020,5,10)
fecha1 = arrow.get(2050,10,5)
resultado = hoy-fecha1

if hoy > fecha1:
    print("Entre", hoy , "y", fecha1, "han pasado", resultado)
else:
    print("Entre", hoy, "y", fecha1, "quedan todavía", resultado)
