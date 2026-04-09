import string

while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if entrada.lower() == "fim":
        break
    
    # Remove espaços e pontuação, e coloca tudo em minúsculo
    frase_limpa = "".join(caractere.lower() for caractere in entrada if caractere.isalnum())
    
    # Inverte a frase limpa usando fatiamento [::-1]
    if frase_limpa == frase_limpa[::-1]:
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')