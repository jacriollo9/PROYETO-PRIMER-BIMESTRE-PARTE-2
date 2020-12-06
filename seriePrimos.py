print ("Ejercicio19")
print ("José Adrián Criollo Jiménez")
print (" Programa para general la serie")

num = 0
den = 1
n = 0
suma = 0
divi= 0
i2 = 1
v = 0

n = int(input("Programa para generar la serie \nIngrese el limite de la serie\n"))

for i in range(1, (n+1)):
    num = i
    v = 0
    while v == 0:
        den = den + 1
        i2 = 1
        for i2 in range(i2, (den+1)):
            if den % i2 == 0:
                divi = divi + 1
        if divi == 2:
            v = 1
        divi = 0
    if i % 2 == 0:
        print(i, " -", +num, " / ", den)
    else:
        print(i, " +", num, " / ", den)
    suma = suma + ((-1) **(i+1)) * (num/den) 

print("------------------------------")
print("La suma de la serie es: ", suma)