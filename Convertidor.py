print ("Ejercicio13")
print ("José Adrián Criollo Jiménez")
print ("Programa para calcular de metros, centimetros, kilometros, pies, pulgadas")

#Declaración y inicilización de variables
Metros = float(0)
Centimetros = float(0)
Kilometros = float(0)
Pie = float(0)
Pulgadas = float(0)

#Ingresa valor en metros
Metros = float (input("Ingrese el valor en metros: "))
Metros = float(Metros)

#Salida de datos

#Calcula la cantidad de metros a centimetros
Centimetros = Metros * 100

#Calcula la cantidad de metros a Kilometros
Kilometros = Metros / 1000

#Calcula la cantidad de metros a Pie
Pie = Metros * 3.28

# Calcula la cantidad de metros a Pulgadas
Pulgada = Metros * 39.37

print ("El valor de metros a centimetros es: %.5f " % Centimetros)
print ("El valor de metros a Kilometros es: %.5f " % Kilometros)
print ("El valor de metros a Pies es: %.5f " % Pie)
print ("El valor de metros a Pulgadas es: %.5f " % Pulgada)
