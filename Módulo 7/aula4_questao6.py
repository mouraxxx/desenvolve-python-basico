arquivo_nome = "spotify-2023.csv"

top_por_ano = {}

try:
    with open(arquivo_nome, 'r', encoding='latin-1') as arquivo:
        print("--- Primeiras 5 linhas do arquivo ---")
        cabecalho = arquivo.readline()
        print(cabecalho.strip())
        for _ in range(4):
            print(arquivo.readline().strip())
        print("-" * 40)

        arquivo.seek(0)
        arquivo.readline() 

        for linha in arquivo:
            if '"' in linha:
                continue
            
            dados = linha.strip().split(',')
            
            try:
                nome = dados[0]
                artista = dados[1]
                ano = int(dados[3])
                streams = int(dados[8])
                
                if 2012 <= ano <= 2022:
                    if ano not in top_por_ano or streams > top_por_ano[ano][3]:
                        top_por_ano[ano] = [nome, artista, ano, streams]
            
            except (ValueError, IndexError):

                continue

    lista_final = []
    for ano in range(2012, 2023):
        if ano in top_por_ano:
            lista_final.append(top_por_ano[ano])

    print("\n--- Top Músicas por Ano (2012-2022) ---")
    for item in lista_final:
        print(item)

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_nome}' não foi encontrado. Certifique-se de que ele está na mesma pasta do script.")