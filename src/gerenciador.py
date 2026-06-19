
tarefas = []

def adicionar_tarefa(id_tarefa, titulo, descricao):
    """
    Função Create: Adiciona uma nova tarefa ao sistema.
    """
    nova_tarefa = {
        "id": id_tarefa,
        "titulo": titulo,
        "descricao": descricao,
        "status": "A Fazer"
    }
    tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas():
    """
    Função Read: Retorna todas as tarefas registradas.
    """
    return tarefas