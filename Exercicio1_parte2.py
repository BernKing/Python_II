# Exercicio1
# Elabore um programa em que o utilizador digite um número à sua escolha e seja impressa
# a respetiva tabuada. 3 x 1 = 3

numero = int(input("Introduza um numero para calcular a tabuada do mesmo:"))


for i in range(1,11):
    print(numero, "x", i, "=", numero*i)

