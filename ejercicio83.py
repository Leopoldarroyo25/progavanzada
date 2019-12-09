#ejercicio83
#Amazon provee envio express para mucho de sus produtos a un costo de $195 por el primer producto y de $29.50 para cada producto subsecuente escriba una funcion 
#que tome el numero de productos y como su unico argumeto. Regrese el costo de envio total como el resultado de la funcion incluya un programa principal que lea
#el numero de productos comprados por el usuario y despligue el numero total de envio
def envio(produc):
if produc ==1:
    total= 195
elif produc >= 2:
    total=195+(29.5*(produc-1))
    
    return total
num=int(input('ingrese numeor de paquetes'))
envit=envio(num)
print('el total es: ', envit)