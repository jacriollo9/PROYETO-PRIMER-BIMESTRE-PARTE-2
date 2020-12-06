print ("Ejercicio17")
print ("José Adrián Criollo Jiménez")
print (" Programa para verificar si un numero es par o impar ")

# Declarar e iniializar las variables

cont = 1
n = 1
num = 0 
SumPar = 0
SumImpar = 0
SumNeg = 0
SumPos = 0

#Ingresa los datos de entrada limite
n= int(input("Ingresa el limite de numeros a verificar: "))

#Crear el ciclo para verificar los numeros 

while cont <= n:
	num= int(input("Ingresa el numero a verificar: "))
	if num % 2 == 0: #Verificar si un numero es par o impar
		SumPar = SumPar + num #Suma los numeros pares 
	else:
		SumImpar = SumImpar + num
	if num > 0:
		SumPos = SumPos + num
	else:
		SumNeg = SumNeg + num
	cont = cont + 1
print ("La suma de los pares es: " ,SumPar)
print ("La suma de los impares es: " ,SumImpar)
print ("La suma de los positivos es: " ,SumPos)
print ("La suma de los negativos es: " ,SumNeg)

