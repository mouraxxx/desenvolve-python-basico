import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")

print(f"Intersecção: {interseccao}")

print("\nContagem:")
for elemento in interseccao:
    qtd_lista1 = lista1.count(elemento)
    qtd_lista2 = lista2.count(elemento)
    print(f"{elemento}: (lista1={qtd_lista1}, lista2={qtd_lista2})")