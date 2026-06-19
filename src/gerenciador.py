tarefas = []

def adicionar_tarefa(id_tarefa, titulo, descricao):
    nova_tarefa = {
        "id": id_tarefa,
        "titulo": titulo,
        "descricao": descricao,
        "status": "A Fazer"
    }
    tarefas.append(nova_tarefa)
    return nova_tarefa

def listar_tarefas():
    return tarefas

def atualizar_tarefa(id_tarefa, novo_status):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = novo_status
            return tarefa
    return None

def remover_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            return True
    return False