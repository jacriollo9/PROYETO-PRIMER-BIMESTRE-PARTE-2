print ("Ejercicio14")
print ("José Adrián Criollo Jiménez")
print ("Programa para determinar la suma de una serie de numeros ")

#Declaración y inicilización de variables

print("Ingrese un numero")
i = 1
n = 0
suma = 0

# Ingresar Datos
n=int(input("Ingrese el limite de números a presentar"))

while i <= n:
	print (i)
	suma=suma+i
	i= i+1
	
print("La suma de los números es: " ,suma)
