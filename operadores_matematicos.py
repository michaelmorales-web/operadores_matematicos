# Programa para invertir un número entero de cuatro cifras

# input
n = input("Digite un número de 4 digitos: ")
n = int(n)

#procesing
r4 = n%10
r3 = (n//10)%10
r2 = (n//100)%10
r1 = (n//1000)%10

ni= r4*1000 + r3*100 + r2*10 + r1

#output
print("-----Resultado-----")
print("Numero original: " + str(n))
print("Utimo digito : " + str(r4))
print("Tercer digito: " + str(r3))
print("Segundo digito: " + str(r2))
print("Primer digito: " + str(r1))
print("El número invertido es: " + str(ni))

