# Lê o valor total em reais
valor = int(input())

# Lista com as notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Armazena o valor original para o cálculo e itera sobre as notas
restante = valor
for nota in notas:
    # Calcula quantas notas cabem no valor atual
    quantidade = restante // nota
    # Atualiza o restante com o que sobrou após as notas calculadas
    restante = restante % nota
    # Imprime a linha formatada exatamente como solicitado
    print(f"{quantidade} nota(s) de R${nota},00")