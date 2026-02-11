distancia = float(input("Digite a distância (km): "))
peso = float(input("Digite o peso do pacote (kg): "))

if distancia <= 100:
    valor_por_kg = 1.00
elif distancia <= 300:
    valor_por_kg = 1.50
else:
    valor_por_kg = 2.00

frete = peso * valor_por_kg

if peso > 10:
    frete += 10

print(f"O valor total do frete é: R${frete:.2f}")