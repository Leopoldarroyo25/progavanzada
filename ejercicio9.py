#(Ejercicio9)
#(Usted acaba de abrir una nueva cuenta de ahorros con el cual gana el 4% de interes por el año. El interes que usted genere es pagado al fin de año, y es agregado al balance de la cuenta de banco. Escriba un programa que comienze por leer la cantidad de dinero depositada en la cuenta (el usuario introduce esta cantidad). El programa debe calcular y mostrar la cantidad de dindero en la cuenta despues del primer, segundo y tercer año. Despliegue las cantidades de dindero redondeado a 2 decimales.)
interes=.4
cantidad=int(input('ingresa catidad de dinero depositado $'))
operacion1= cantidad * interes
n = cantidad + operacion1
print("dinero el primer $%.2f." % n)
operacion2= n*interes
print("dinero el segundo $%.2f." % (operacion2 +n)) 
operacion3= (operacion2 + n)*interes
operacion4=operacion3+ (operacion2 +n)
print("dinero el tercero $%.2f." % (operacion4))
