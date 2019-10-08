#(Escriba un programa que determine como un objeto viaja cuando golpea el piso. El usuario inserta la información de la altura desde donde el objeto se deja caer, en metros(m). Dado que el objeto se deja caer desde el reposo(velocidad inicial V0m/s). Asumiendo que la aceleración debido a la gravedad es 9.81m/s¨2 y usando la formula Vf=raiz(V0¨2 +2gd) calcule la velocidad final Vf usando la velocidad inicial V0 la aceleracion g y la distancia d).
import math

d=int(input('ingrese distancia'))
g=9.81
V0=0
formula= math.sqrt((math.pow(V0, 2) + (2*g)*(d)))
print('Vf =',' %.4f''m/s' % formula)