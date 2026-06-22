tarefas = []

def adicionar_tarefa(id_tarefa, titulo, descricao, operador="Não atribuído"):
    nova_tarefa = {
        "id": id_tarefa,
        "titulo": titulo,
        "descricao": descricao,
        "status": "A Fazer",
        "operador": operador
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

def listar_por_operador(nome_operador):
    return [tarefa for tarefa in tarefas if tarefa["operador"] == nome_operador]