# Lê o comprimento do terreno
comprimento = int(input("Digite o comprimento: "))
# Lê a largura do terreno
largura = int(input("Digite a largura: "))
# Lê o preço do metro quadrado
preco_m2 = float(input("Digite o preço por m2: "))

# Calcula a área multiplicando comprimento por largura
area_m2 = comprimento * largura
# Calcula o preço total multiplicando a área pelo preço do metro quadrado
preco_total = preco_m2 * area_m2

# Imprime o resultado formatado com a área em metros quadrados e o preço total em reais.
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")