frase = input("Digite uma frase: ")

vogais_referencia = "aeiouAEIOU"

vogais = sorted([char for char in frase if char in vogais_referencia])

consoantes = [char for char in frase if char.isalpha() and char not in vogais_referencia]

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")