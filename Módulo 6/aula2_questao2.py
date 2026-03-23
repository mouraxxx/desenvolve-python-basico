import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print(f"Lista elementos (tamanho {num_elementos}): {elementos}")

soma = sum(elementos)
print(f"Soma dos valores: {soma}")

media = soma / num_elementos
print(f"Média dos valores: {media:.2f}")