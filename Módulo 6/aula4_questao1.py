pares_20_50 = [x for x in range(20, 51) if x % 2 == 0]

lista_base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in lista_base]

divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

paridade = ["par" if x % 2 == 0 else "impar" for x in range(0, 30, 3)]

print(f"Pares (20-50): {pares_20_50}")
print(f"Quadrados: {quadrados}")
print(f"Divisíveis por 7: {divisiveis_por_7}")
print(f"Paridade (step 3): {paridade}")