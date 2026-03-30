frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

palavras = frase.split()

objetivo_ordenado = sorted(objetivo.lower())

anagramas = []

for p in palavras:
    if len(p) == len(objetivo):
        if sorted(p.lower()) == objetivo_ordenado:
            anagramas.append(p)

print(f"Anagramas: {anagramas}")