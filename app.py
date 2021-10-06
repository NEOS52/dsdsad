numero = input("pasa el numero: ")

cont= 0

for i in range (numero):
    if numero % i == 0:
        cont= cont+1

if cont == 2:
    print("el numero ", numero, "es primo")
else:
    print("el numero ", numero, "no es primo")