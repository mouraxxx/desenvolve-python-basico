import re

nome_arquivo = "estomago.txt"

try:
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    print("--- Primeiras 25 linhas ---")
    for linha in linhas[:25]:
        print(linha.strip())

    total_linhas = len(linhas)
    print(f"\nTotal de linhas no arquivo: {total_linhas}")

    linha_longa = max(linhas, key=len)
    print(f"\nA linha mais longa tem {len(linha_longa)} caracteres.")

    texto_completo = "".join(linhas).lower()

    contagem_nonato = len(re.findall(r'\bnonato\b', texto_completo))
    contagem_iria = len(re.findall(r'\bíria\b', texto_completo))

    print(f"Menções a 'Nonato': {contagem_nonato}")
    print(f"Menções a 'Íria': {contagem_iria}")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")