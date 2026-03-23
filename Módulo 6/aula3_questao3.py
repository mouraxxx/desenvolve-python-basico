import random

lista = [random.randint(-10, 10) for _ in range(20)]

print(f"Original: {lista}")

max_negativos = -1
inicio_intervalo = 0
tamanho_janela = 3

for i in range(len(lista) - tamanho_janela + 1):
    janela = lista[i : i + tamanho_janela]
    contagem_negativos = sum(1 for x in janela if x < 0)
    
    if contagem_negativos > max_negativos:
        max_negativos = contagem_negativos
        inicio_intervalo = i

del lista[inicio_intervalo : inicio_intervalo + tamanho_janela]

print(f"Editada:  {lista}")