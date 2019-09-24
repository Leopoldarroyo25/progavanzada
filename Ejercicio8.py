#(Un vendedor de una pagina de abarrotes en linea vende dos tipos de cajas de cereal. CornFlakes de 750gr y Trix de 500gr. Escriba un programa que lea el numero de cajas de CornFlakes y cajas de Trix, cuyo valor debe ser introducido por el usuario. Despues su programa debe calcular y mostrar el total del peso (en kilogramos) del envio.)
CFK=.750
TXK=.500
CFN=int(input('Ingrese cantidad de CornFlakes'))
TXN=int(input('Ingrese cantidad de CornFlakes'))
operacionCFC=CFN*CFK
operacionTXC=TXN*TXK
print("total de CornFlakes",operacionCFC, 'kilogramos') 
print( "total de Trixis",operacionTXC, 'Kilogramos')

