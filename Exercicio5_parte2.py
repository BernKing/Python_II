#  Exercicio 5
# No dia da estreia do filme "À procura de Dory", uma grande emissora de TV realizou uma
# pesquisa logo após o encerramento do filme. Cada espectador respondeu a um
# questionário no qual constava a sua idade e a sua opinião em relação ao filme: excelente
# - 3; bom - 2; regular - 1. Crie um programa que receba a idade e a opinião de 20
# espectadores, calcule e imprima:
# • A média das idades das pessoas que responderam “excelente”;
# • A quantidade de pessoas que responderam “regular”;
# • A percentagem de pessoas que responderam “bom”, de entre todos os
# espectadores analisados.

# Dicionario

idade = []
opiniao = []

idade_soma = 0
contador_idade = 0
regular = 0
bom = 0
for i in range(5):
    idade.append(int(input("Introduza a sua idade: ")))
    while True:
        opiniaotemp = int(input("Introduza uma nota de 1 a 3: "))
        if 1 <= opiniaotemp <= 3:
            opiniao.append(opiniaotemp)
            break

for i in range(5):
    if opiniao[i] == 3:
        idade_soma += idade[i]
        contador_idade += 1
    if opiniao[i] == 1:
        regular += 1
    if opiniao[i] == 2:
        bom += 1

media = idade_soma / contador_idade
percentagem = (bom * 100) / 5
print("Media de idade das respostas excelentes(3): ", media)
print("Quantidade de pessoas que responderam regular: ", regular)
print("Percentagem de pessoas que responderam bom: ", percentagem,"%")
