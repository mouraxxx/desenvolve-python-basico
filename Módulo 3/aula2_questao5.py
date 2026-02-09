genero = input("Digite seu gênero (M/F): ").upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (anos): "))

regra_a = (genero == "F" and idade > 60) or (genero == "M" and idade > 65)

regra_b = tempo_servico >= 30

regra_c = idade >= 60 and tempo_servico >= 25

pode_aposentar = regra_a or regra_b or regra_c
print(pode_aposentar)