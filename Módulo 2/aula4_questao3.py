# Processamento do Produto 1
nome1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o preço unitário do produto 1:"))
qtd1 = int(input("Digite a quantidade do produto 1:"))

# Processamento do Produto 2
nome2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o preço unitário do produto 2:"))
qtd2 = int(input("Digite a quantidade do produto 2:"))

# Processamento do Produto 3
nome3 = input("Digite o nome do produto 3:")
preco3 = float(input("Digite o preço unitário do produto 3:"))
qtd3 = int(input("Digite a quantidade do produto 3:"))

# Cálculo do total geral
total = (preco1 * qtd1) + (preco2 * qtd2) + (preco3 * qtd3)

# Imprime o total geral
print(f"Total: R${total:,.2f}")