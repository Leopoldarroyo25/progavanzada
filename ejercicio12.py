#ejercicio12(Distancia entre dos puntos)
#(La superficie de la Tierra es curva y la distancia entre grados de longitud varia con la latitud. Como resultado, encontrar la distanci entre dos puentos de la superficie de la tierra es mas complicado que usar el Teorema de Pitágoras. Si (t1,g1) y (t2,g2) es la latitud y longitud de dos puntos de la superficie de la tierra. La distancia entre esos puntos, a traves de la superficie de la tierra, en Kilometros es:)
#(Creeun progreama que le permita al usuario introducir la latitus y longitud de dos puntos de la tierra en grados. Su programa debe desplegar la distancia entre esos puntos, en kilometros. Tenga en cuenta que las funciones trigronometricas en python trabajan en radianes, por lo que debe de convertir el valor introducido por el usuario en grados a comandos radianes, que cambia de grados a radianes.)

import math
di1=int(input('ingrese valor distancia 1 '))
ga1=int(input('ingrese valor grados 1 '))
di2=int(input('ingrese valor distancia 2 '))
ga2=int(input('ingrese valor grados 2 '))
g1= math.radians (ga1)
g2= math.radians (ga2)
t1= math.radians (di1)
t2= math.radians (di2)

distancia= 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1-g2))
print('Distancia entre puntos', distancia)