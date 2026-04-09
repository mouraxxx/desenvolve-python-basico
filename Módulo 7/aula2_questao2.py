frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
frase_modificada = ""

for letra in frase:
    if letra in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += letra

print(f"Frase modificada: {frase_modificada}")