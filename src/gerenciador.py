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