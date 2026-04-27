import csv
from collections import namedtuple
from getpass import getpass

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

# --- CONSTANTES ---
ARQUIVO_USUARIOS = 'usuarios.txt'
ARQUIVO_JOGADORES = 'jogadores.txt'
USUARIO_LOGADO = None

# --- ESTRUTURAS DE DADOS (Named Tuples) ---
Usuario = namedtuple('Usuario', ['login', 'senha', 'tipo'])
Jogador = namedtuple('Jogador', ['nome', 'preco', 'clube'])

##################### FUNÇÕES DE USUÁRIO (CRUD) #####################

def ler_usuarios(arquivo_csv):
    """CRUD (Read): Lê os usuários do arquivo txt."""
    usuarios = {}
    try:
        with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    u = Usuario(login=row[0], senha=row[1], tipo=row[2])
                    usuarios[u.login] = u
    except FileNotFoundError:
        console.print("[red]Arquivo de usuários não encontrado. Criando novo...[/]")
    return usuarios

def fazer_login(usuarios):
    """Controle de Acesso."""
    global USUARIO_LOGADO
    console.print(Panel("⚽ [bold green]Login FootStats Pro[/bold green] ⚽", expand=False))
    username = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")

    user = usuarios.get(username)
    if user and user.senha == senha:
        console.print("\n[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = user
    else:
        console.print("[bold red]Erro: usuário ou senha incorretos![/bold red]")

def cadastrar_usuario(usuarios, arquivo_csv):
    """CRUD (Create): Cadastra novo usuário."""
    console.print(Panel("📝 [bold green]Cadastro[/bold green]", expand=False))
    login = Prompt.ask("[bold cyan]Novo Login[/bold cyan]")
    
    if login in usuarios:
        console.print("[bold red]Erro: Usuário já existe![/bold red]")
        return False
        
    senha = getpass("Senha: ")
    tipo = 'cliente'
    if USUARIO_LOGADO and USUARIO_LOGADO.tipo == 'admin':
        tipo = Prompt.ask("Tipo", choices=["admin", "cliente"])

    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([login, senha, tipo])
    console.print(f"[bold green]Usuário {login} cadastrado![/bold green]")
    return login

##################### FUNÇÕES DE JOGADORES (CRUD) #####################

def ler_jogadores(arquivo_csv):
    """CRUD (Read): Carrega os produtos (jogadores) do arquivo."""
    jogadores = []
    try:
        with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    jogadores.append(Jogador(nome=row[0], preco=float(row[1]), clube=row[2]))
    except FileNotFoundError:
        pass
    return jogadores

def salvar_jogadores(jogadores, arquivo_csv):
    """CRUD (Update/Delete/Create): Persiste a lista atualizada no arquivo."""
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for j in jogadores:
            writer.writerow([j.nome, j.preco, j.clube])

def exibir_tabela_jogadores(lista_jogadores):
    """Função auxiliar para imprimir os registros formatados."""
    table = Table(title="📊 Mercado de Transferências") # type: ignore
    table.add_column("Nome", style="cyan")
    table.add_column("Preço (€ Mi)", justify="right", style="green")
    table.add_column("Clube", style="magenta")
    for j in lista_jogadores:
        table.add_row(j.nome, f"{j.preco:.1f}", j.clube)
    console.print(table)

##################### MENUS #####################

def menu_inicial():
    console.print(Panel("[bold green]FOOTSTATS PRO[/bold green]\nSistema de Gestão Esportiva", title="Início", expand=False))
    console.print("[1] Fazer Login\n[2] Cadastro\n[3] Sair")
    return Prompt.ask("Opção", choices=["1", "2", "3"])

def menu_interno():
    console.print(Panel(f"👤 [bold]Usuário:[/bold] {USUARIO_LOGADO.login} | [bold]Nível:[/bold] {USUARIO_LOGADO.tipo}", expand=False))
    console.print("[1] Listar Jogadores (por Nome)\n[2] Listar Jogadores (por Preço)\n[3] Buscar Jogador")
    
    if USUARIO_LOGADO.tipo == 'admin':
        console.print("[4] Adicionar Jogador (C)\n[5] Remover Jogador (D)")
    
    console.print("[0] Logout")
    return Prompt.ask("Escolha")

# --- FLUXO PRINCIPAL ---
def main():
    global USUARIO_LOGADO
    while True:
        usuarios = ler_usuarios(ARQUIVO_USUARIOS)
        
        if not USUARIO_LOGADO:
            opcao = menu_inicial()
            if opcao == "1": fazer_login(usuarios)
            elif opcao == "2": cadastrar_usuario(usuarios, ARQUIVO_USUARIOS)
            else: break
        else:
            jogadores = ler_jogadores(ARQUIVO_JOGADORES)
            escolha = menu_interno()
            
            if escolha == "0":
                USUARIO_LOGADO = None
            elif escolha == "1":
                exibir_tabela_jogadores(sorted(jogadores, key=lambda x: x.nome))
            elif escolha == "2":
                exibir_tabela_jogadores(sorted(jogadores, key=lambda x: x.preco, reverse=True))
            elif escolha == "3":
                busca = Prompt.ask("Digite o nome").lower()
                resultado = [j for j in jogadores if busca in j.nome.lower()]
                exibir_tabela_jogadores(resultado)
            elif escolha == "4" and USUARIO_LOGADO.tipo == 'admin':
                n = Prompt.ask("Nome do Atleta")
                p = float(Prompt.ask("Preço (€ Milhões)"))
                c = Prompt.ask("Clube Atual")
                jogadores.append(Jogador(n, p, c))
                salvar_jogadores(jogadores, ARQUIVO_JOGADORES)
            elif escolha == "5" and USUARIO_LOGADO.tipo == 'admin':
                nome_del = Prompt.ask("Nome exato para remover")
                jogadores = [j for j in jogadores if j.nome != nome_del]
                salvar_jogadores(jogadores, ARQUIVO_JOGADORES)