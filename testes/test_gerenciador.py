
from src.gerenciador import tarefas, adicionar_tarefa, listar_tarefas, atualizar_tarefa, remover_tarefa

def test_adicionar_tarefa():
    tarefas.clear()
    tarefa = adicionar_tarefa(1, "Comprar pão", "Ir à padaria")
    assert tarefa["id"] == 1
    assert tarefa["titulo"] == "Comprar pão"
    assert len(tarefas) == 1

def test_listar_tarefas():
    tarefas.clear()
    adicionar_tarefa(1, "Estudar", "Estudar Git")
    adicionar_tarefa(2, "Ler", "Ler livro de UML")
    lista = listar_tarefas()
    assert len(lista) == 2

def test_atualizar_tarefa():
    tarefas.clear()
    adicionar_tarefa(1, "Correr", "Correr 5km")
    tarefa_atualizada = atualizar_tarefa(1, "Concluído")
    assert tarefa_atualizada["status"] == "Concluído"

def test_remover_tarefa():
    tarefas.clear()
    adicionar_tarefa(1, "Limpar a casa", "Faxina geral")
    resultado = remover_tarefa(1)
    assert resultado is True
    assert len(tarefas) == 0