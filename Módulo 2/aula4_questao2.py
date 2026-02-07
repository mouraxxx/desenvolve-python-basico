# Lê a temperatura em Fahrenheit
f = int(input("Digite a temperatura em Fahrenheit: "))

# Aplica a fórmula de conversão para Celsius
c_float = (f - 32) * (5/9)
# Converte o resultado de Celsius para um número inteiro
c_int = int(c_float)

# Exibe a mensagem formatada com a temperatura em Fahrenheit e a correspondente temperatura em Celsius
print(f"{f} graus Fahrenheit são {c_int} graus Celsius.")