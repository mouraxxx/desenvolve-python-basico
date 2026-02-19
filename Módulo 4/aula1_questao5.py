N = int(input("Digite a quantidade de respondentes: "))

soma_idades = 0
contador = 0

while contador < N:
    idade = int(input(f"Digite a idade do respondente {contador + 1}: "))
    soma_idades += idade
    contador += 1

if N > 0:
    media = soma_idades / N
    print(f"A média de idade dos respondentes é: {media:.2f}")
else:
    print("Nenhum respondente cadastrado.")