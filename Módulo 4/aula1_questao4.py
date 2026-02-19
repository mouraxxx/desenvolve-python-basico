n = int(input("Quantos números você deseja comparar? "))
maior = 0

while n > 0:
    x = float(input("Digite um número: "))
    
    if x > maior:
        maior = x
    
    n = n - 1

print(f"O maior número digitado foi: {maior}")