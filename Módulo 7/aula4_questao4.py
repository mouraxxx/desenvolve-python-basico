import random

def imprime_enforcado(erros, estagios):
    """Imprime o desenho do enforcado com base no número de erros."""
    print(estagios[erros])

def jogar():
    try:
        with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
            palavras = [linha.strip().upper() for linha in f.readlines() if linha.strip()]
        palavra_secreta = random.choice(palavras)
    except FileNotFoundError:
        print("Erro: Arquivo 'gabarito_forca.txt' não encontrado.")
        return

    try:
        with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()
            estagios = conteudo.split("=========")
            estagios = [e.strip() + "\n=========" for e in estagios if e.strip()]
    except FileNotFoundError:
        print("Erro: Arquivo 'gabarito_enforcado.txt' não encontrado.")
        return

    letras_descobertas = ["_" for _ in palavra_secreta]
    letras_tentadas = []
    erros = 0
    max_erros = 6

    print("*** BEM-VINDO AO JOGO DA FORCA ***")
    
    while erros < max_erros and "_" in letras_descobertas:
        print("\n" + " ".join(letras_descobertas))
        print(f"Letras já tentadas: {', '.join(letras_tentadas)}")
        
        chute = input("Digite uma letra: ").strip().upper()

        # Validação simples
        if not chute or len(chute) > 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue
        
        if chute in letras_tentadas:
            print(f"Você já tentou a letra '{chute}'. Tente outra!")
            continue

        letras_tentadas.append(chute)

        if chute in palavra_secreta:
            print(f"Boa! A letra '{chute}' existe na palavra.")
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[i] = chute
        else:
            erros += 1
            print(f"Ops! A letra '{chute}' não existe.")
            imprime_enforcado(erros, estagios)

    if "_" not in letras_descobertas:
        print("\n" + " ".join(letras_descobertas))
        print("PARABÉNS! Você venceu! 🏆")
    else:
        print(f"\nQUE PENA! Você foi enforcado. 💀")
        print(f"A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogar()