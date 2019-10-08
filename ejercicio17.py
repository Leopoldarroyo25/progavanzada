#Ejercicio 17
#The amount of energy required to increase the temperature of one gram of a material
#by one degree Celsius is the material’s specific heat capacity, C. The total amount
#of energy required to raise m grams of a material by ΔT degrees Celsius can be
#computed using the formula:
#q = mCΔT.
#Write a program that reads the mass of some water and the temperature change
#from the user. Your program should display the total amount of energy that must be
#added or removed to achieve the desired temperature change.

agua=4.186
ele= 8.9
J= 2.7777e-7

Volumen =float(input("inserte los mililitros de agua:"))
Dtemperatura=float(input( "inserte la temperatura en grados celcius:"))
q= Volumen * Dtemperatura * agua
print (" usted requiere %d joules de energia" % q )
kilovatios= q*J
costo =kilovatios * ele
print ( "la energia del costo  es en  centavos  : ", costo)



