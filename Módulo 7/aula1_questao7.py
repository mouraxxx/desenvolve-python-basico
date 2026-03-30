import random

def encrypt(lista_nomes):
    n = random.randint(1, 10)
    nomes_criptografados = []
    
    for nome in lista_nomes:
        nome_cripto = ""
        for caractere in nome:
            codigo = ord(caractere)
            novo_codigo = codigo + n
            if novo_codigo > 126:
                novo_codigo = 33 + (novo_codigo - 127)
            nome_cripto += chr(novo_codigo)
        nomes_criptografados.append(nome_cripto)
        
    return nomes_criptografados, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)

print(f"Chave gerada: {chave}")
print(f"Nomes originais: {nomes}")
print(f"Nomes criptografados: {nomes_cript}")