# Exercicio2
# Elabore um programa que conte os números pares entre dois números quaisquer

num1 = int(input("Introduza o primeiro numero:"))
num2 = int(input("Introduza o segundo numero:"))
pares = 0

for i in range(num1 + 1, num2 + 1):

    if i % 2 == 0:
        pares += 1

print("Numero de pares = ",pares)