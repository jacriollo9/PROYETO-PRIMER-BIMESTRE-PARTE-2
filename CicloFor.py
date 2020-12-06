print ("Ejercicio23")
print ("José Adrián Criollo Jiménez")
print ("Programa para calcular la serie de fibonacci")

n = 0 
primero = 0
segundo = 1
fibo = 0
suma = 0
suma1 = 0

n = int(input("Ingrese el limite de la serie fibonacci"))

for i in range (1,n):
	if i < 2:
		print (i , ", " ,primero)
		print ( i  + 1, ", " ,segundo)
		suma = primero + segundo
		i = i + 1
	else:
		fibo = primero + segundo
		suma = suma + fibo
		primero = segundo
		segundo = fibo

		print(i , ", " ,fibo)
print("\n PRIMERA SUMA:" ,suma)
print ("Segunda solucion")

primero = 0 
segundo = 1 
fibo = 0
for i in range (1,n+1):
	print (i , " ," ,primero)
	suma1 = suma1 + primero
	fibo = primero + segundo
	primero = segundo
	segundo = fibo
print ("\n SEGUNDA SUMA:" ,suma1)