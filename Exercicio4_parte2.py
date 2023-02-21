# Exercicio4

# Elabore um programa que receba, via teclado, uma frase e uma letra e retorne o número
# de vezes essa letra existe na frase e em que posições.

frase = input("Introduza uma frase:")
letra = input("Introduza a letra que pretende contar:")
contador_letra = 0
posicoes = []
contadorposicoes = 0


for char in frase:

    if char.lower() in letra:
        contador_letra += 1
        posicao = frase.find(letra, contadorposicoes)
        posicoes.append(posicao)

    contadorposicoes += 1

# Posicoes começam com 0
print("A letra ",letra,"apareceu:",contador_letra, "vezes")

for i in range(len(posicoes)):
    print("A letra estava na posicao: ",posicoes[i])