# Exericio3
# Elabore um programa que receba uma frase e conte o número de vogais existente na
# frase

frase = input("Introduza uma frase:")

#char.lower() converte a string para letras minusculas

vogais = 0
for char in frase:
    if char.lower() in "aeiou":
        vogais += 1

print("Esta frase contem: ",vogais, "vogais")