livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", "2003", "368"],
    ["Torto Arado", "Itamar Vieira Junior", "2019", "264"],
    ["Dom Casmurro", "Machado de Assis", "1899", "256"],
    ["1984", "George Orwell", "1949", "336"],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1943", "96"],
    ["O Hobbit", "J.R.R. Tolkien", "1937", "310"],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", "1997", "223"],
    ["O Alquimista", "Paulo Coelho", "1988", "208"],
    ["Ensaio Sobre a Cegueira", "José Saramago", "1995", "312"],
    ["A Hora da Estrela", "Clarice Lispector", "1977", "88"]
]

nome_arquivo = "meus_livros.csv"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    for livro in livros:
        linha = ",".join(livro) + "\n"
        arquivo.write(linha)

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")