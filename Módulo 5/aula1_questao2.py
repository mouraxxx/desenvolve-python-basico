import random
import math

n = int(input("Digite a quantidade de números (n): "))
soma = 0

for _ in range(n):
    numero_aleatorio = random.randint(0, 100)
    soma += numero_aleatorio
print(f"Gerado: {numero_aleatorio}")

raiz_quadrada = math.sqrt(soma)

print(f"A soma dos valores gerados é: {soma}")
print(f"A raiz quadrada da soma é: {raiz_quadrada:.2f}")