"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Bem-vindo ao Desafio de Git!"
    """
    return "Bem-vindo ao Desafio de Git!"

def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    # A lista de comandos deve ser implementada aqui
    return ["git init", "git add", "git commit", "git status", "git push", "git clone", "git pull"]


def criar_mensagem_commit(funcao_nome):
    """
    Recebe o nome de uma função e retorna uma mensagem de commit padronizada.
    Exemplo:
    criar_mensagem_commit("listar_comandos_git_basicos") ->
    "Implementa função listar_comandos_git_basicos"
    """
    # Sua solução:
    return f"Implementa função {funcao_nome}"


def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    # Verifica o formato 'v<digito>.<digito>'
    padrao = r'^v\d+\.\d+$'
    return bool(re.match(padrao, tag))


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.
    ...
    """
    # Solução para a Tarefa #5
    num_funcoes = len(funcoes_concluidas)
    return f"Desafio concluído! {num_funcoes} funções implementadas com sucesso."
