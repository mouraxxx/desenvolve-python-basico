frase = input("Digite uma frase: ")

vogais_referencia = "aeiou"
indices = []

for i, letra in enumerate(frase):
    if letra.lower() in vogais_referencia:
        indices.append(i)

print(f"{len(indices)} vogais")
print(f"Índices {indices}")