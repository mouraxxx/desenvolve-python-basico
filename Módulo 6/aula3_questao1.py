numeros = []

print("Digite números inteiros. (Digite 'fim' para encerrar)")

while True:
    entrada = input(f"Digite o {len(numeros) + 1}º número: ")
    
    if entrada.lower() == 'fim':
        if len(numeros) < 4:
            print("Erro: Você precisa digitar pelo menos 4 números.")
            continue
        else:
            break
    
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("\n" + "="*30)
print("RESULTADOS DO FATIAMENTO")
print("="*30)

print(f"Lista original: {numeros}")

print(f"Os 3 primeiros elementos: {numeros[:3]}")

print(f"Os 2 últimos elementos: {numeros[-2:]}")

print(f"Lista invertida: {numeros[::-1]}")

print(f"Elementos de índice par: {numeros[::2]}")

print(f"Elementos de índice ímpar: {numeros[1::2]}")