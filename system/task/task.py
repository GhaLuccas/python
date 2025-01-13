"""
Desafio: Sistema de Agendamento de Tarefas
Enunciado:
Você vai criar um sistema simples para gerenciar tarefas diárias. 
O sistema permitirá que o usuário adicione, remova e liste tarefas de um dia. 
Cada tarefa deve ter um nome, uma descrição e uma hora de execução. 
O objetivo do sistema é permitir que o usuário agende suas tarefas, 
veja as tarefas agendadas e remova tarefas quando necessário.

Requisitos:

Tarefa:
Cada tarefa tem um nome (string), uma descrição (string) e um horário de execução (string no formato "HH:MM").

Funções do Sistema:
Adicionar tarefa: O usuário deve poder adicionar uma nova tarefa com nome, descrição e horário.
Remover tarefa: O usuário pode remover uma tarefa pelo nome.
Listar tarefas: O sistema deve listar todas as tarefas agendadas com o nome, descrição e horário.

Comandos:
O usuário deve ser capaz de interagir com o sistema por meio de um menu simples. O menu terá as seguintes opções:
1: Adicionar tarefa.
2: Remover tarefa.
3: Listar tarefas.
4: Sair.

Funcionalidades:
Adicionar tarefa: Ao adicionar uma tarefa, o sistema deve pedir o nome, a descrição e o horário da tarefa.
Remover tarefa: O sistema deve pedir o nome da tarefa e, se a tarefa existir, removê-la da lista.
Listar tarefas: O sistema deve exibir todas as tarefas cadastradas, incluindo nome, descrição e horário.

Opções adicionais (para um bônus):
Permitir que o usuário busque tarefas por horário (por exemplo, listar todas as tarefas que começam após determinado horário).
Garantir que não existam duas tarefas com o mesmo nome.

"""

from datetime import datetime
from typing import * 

class Task():
    def __init__(self, taskid:int ,title:str , context:str , time:str):
        self.taskid = taskid
        self.title = title
        self.context = context
        self.time = time
    
    def __str__(self):
        return f'Task: {self.title} -- {self.context}'

class TaskList():
    """Task model"""
    def __init__(self , lista:list):
        self.name = "Lista de Tarefas"
        self.lista = lista
    
    def __str__(self):
        return f'A Lista de tarefas tem {len(self.lista)} tarefas'
    
    """
    bellow are input data validation
    the names are self explanatory
    """
    
    def generate_id(self):
        if self.lista:
            return max(task.taskid for task in self.lista) + 1
    
    def get_valid_id(self):
        if self.lista:
            while True:
                try:
                    id_input = int(input("type the id: "))
                    if id_input >0 and id_input<= max(task.taskid for task in self.lista):
                        print("Valid ID")
                        return id_input
                    else:
                        raise ValueError("invalid ID")
                except ValueError as e :
                    print(f"Error {e} , Please type an valid interege number")
                except Exception as e:
                    print(f'Erros {e} ,unusual error please try again.')
        else:
            print("valid ID")
            return 1
    
    def get_valid_time(self):
        while True:
            try:
                input_time = str(input("Type the time: "))
                valid_time = datetime.strptime(input_time, "%H:%M")
                return valid_time
            except ValueError as e:
                print(f"Erro {e} , please try again.")
            except Exception as  e:
                print(f'Error {e}, Trey again.')
    
    """
    bellow are the system functionalities
    the names are self explanatory
    """
    
    def list_all_task(self)->print:
        ("Listing all task's")
        if self.lista:
            [print(task) for task in self.lista]
        else:
            return print("No task's in the List")

    def list_task_pertime(self):
        print("Listing")
        time = self.get_valid_time()
        [print(task) for task in self.lista if task.time == time]
        
    def add_task(self)->None:
        print("Let's add a new task")
        taskid = self.generate_id()
        title = str(input("Type title: "))
        context= str(input("type the context: "))
        time = self.get_valid_time()
        newtask = Task(taskid , title,context,time)
        self.lista.append(newtask)
        print("Task created sucessfuly")
    
    def remove_task(self)->None:
        print("Let's remove a task")
        taskid = self.get_valid_id()
        for task in self.lista:
            if task.taskid == taskid:
                print(f"Task {task} removed sucessfuly")
                self.lista.remove(task)


test=Task(1,'test1' , 'teting', '12:00')

lista = TaskList([test])
lista.list_all_task()
lista.add_task()
lista.list_all_task()
lista.remove_task()
lista.list_all_task()