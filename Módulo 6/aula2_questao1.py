import random

lista_original = [random.randint(-100, 100) for _ in range(20)]

lista_ordenada = sorted(lista_original)
print(f"Lista Ordenada: {lista_ordenada}")

print(f"Lista Original: {lista_original}")

maior_valor = max(lista_original)
indice_maior = lista_original.index(maior_valor)
print(f"Índice do maior valor ({maior_valor}): {indice_maior}")

menor_valor = min(lista_original)
indice_menor = lista_original.index(menor_valor)
print(f"Índice do menor valor ({menor_valor}): {indice_menor}")