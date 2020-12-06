print ("Ejercicio16")
print ("José Adrián Criollo Jiménez")
print ("Programa que permita encontrar la potencia de un numero")

# Declarar e iniializar las variables

base = 0
pot = 0
cont = 1 
result = 1

#Ingresar los datos

base= int(input("Ingresar la base de la potencia: "))

pot = int(input("Ingresar la potencia: "))


#Ciclo repetitivo que obtiene la potencia deun numero

while cont <= pot:
		result = result * base
		cont = (cont + 1)

#Presentar el resultado	
print ("La potencia es: " , base, " elevado a " , pot, " es: " ,result)
