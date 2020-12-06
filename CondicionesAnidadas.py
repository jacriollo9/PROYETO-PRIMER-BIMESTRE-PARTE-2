print ("Ejercicio15")
print ("José Adrián Criollo Jiménez")
print ("Programa que permita introduciendo una serie de numeros indeterminados su suma no tiene que superar el valor de 10000")

#Inicialización de variables 

media = 0
suma = 0
i = 0
num = 0
sum1 = 0

# Ciclo

while suma <= 10000:
	num = int(input("Ingrese el valor de num: "))
	suma = suma + num
	i = i + 1
	if suma > 10000:
		suma = suma - num	
		print(" Total acumulado es: " ,suma)
		print(" El total de números ingresados es: " ,(i-1))
		media = suma / (i-1)
		print(" La media es: " ,media)
