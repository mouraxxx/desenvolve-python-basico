import re

with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

palavras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', conteudo)

with open("palavras.txt", "w", encoding="utf-8") as arquivo_palavras:
    for palavra in palavras:
        arquivo_palavras.write(palavra + "\n")

print("\nConteúdo de 'palavras.txt':")
with open("palavras.txt", "r", encoding="utf-8") as arquivo_palavras:
    print(arquivo_palavras.read())