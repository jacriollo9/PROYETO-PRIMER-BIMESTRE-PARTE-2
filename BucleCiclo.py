print ("Ejercicio21")
print ("José Adrián Criollo Jiménez")
print ("Programa para obtener los multiplos de cinco")

m5 = 0


for i in range (0,101):
	
	m5 = 0
	while m5 == 0:
		if i % 5 == 0:
			m5 = 1
			print (i)
		else:
			m5 = 1