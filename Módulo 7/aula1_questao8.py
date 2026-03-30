cpf_input = input("Digite o CPF (XXX.XXX.XXX-XX): ")

cpf_numeros = ""
for char in cpf_input:
    if char.isdigit():
        cpf_numeros += char

if len(cpf_numeros) != 11:
    print("Inválido (Quantidade de dígitos incorreta)")
else:
    nove_digitos = cpf_numeros[:9]
    verificadores_reais = cpf_numeros[9:]

    soma_1 = 0
    multiplicador = 10
    for digito in nove_digitos:
        soma_1 += int(digito) * multiplicador
        multiplicador -= 1
    
    resto_1 = soma_1 % 11
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1

    dez_digitos = nove_digitos + str(digito_1)
    soma_2 = 0
    multiplicador = 11
    for digito in dez_digitos:
        soma_2 += int(digito) * multiplicador
        multiplicador -= 1
        
    resto_2 = soma_2 % 11
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2

    digitos_calculados = str(digito_1) + str(digito_2)

    if digitos_calculados == verificadores_reais:
        print("Válido")
    else:
        print("Inválido")