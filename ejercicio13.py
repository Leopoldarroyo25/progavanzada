#ejercicio13
#Consider the software that runs on a self-checkout machine. One task that it must be
#able to perform is to determine how much change to provide when the shopper pays
#for a purchase with cash.
#Write a program that begins by reading a number of cents from the user as an
#integer. Then your program should compute and display the denominations of the
#coins that should be used to give that amount of change to the shopper. The change
#should be given using as few coins as possible. Assume that the machine is loaded
#with pennies, nickels, dimes, quarters, loonies and toonies.
total = float (input('total a pagar:'))
efectivo = float (input('cantidad en efectivo:'))
cambio=efectivo-total
print('cambio  $',cambio)