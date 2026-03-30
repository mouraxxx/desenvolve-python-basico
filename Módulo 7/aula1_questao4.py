celular = input("Digite o número: ")

if len(celular) == 8:
    celular = "9" + celular
elif len(celular) == 9:
    if celular[0] != '9':
        print("Aviso: O número de 9 dígitos não começa com 9.")
else:
    print("Erro: O número deve ter 8 ou 9 dígitos.")

numero_formatado = celular[:-4] + "-" + celular[-4:]

print(f"Número completo: {numero_formatado}")