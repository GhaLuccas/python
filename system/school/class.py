"""

Desafio: Sistema de Gerenciamento de Alunos
Enunciado:
Crie um programa para gerenciar alunos de uma escola. O sistema deve permitir criar e gerenciar alunos, armazenando as seguintes informações:

ID (único para cada aluno).
Nome.
Idade.
Série.

Você deve implementar as seguintes funcionalidades:

Classe Student:
Representa um aluno com os atributos id, name, age e grade.
Implemente o método __str__ para retornar as informações do aluno como uma string formatada.

Classe School:
Gerencia a lista de alunos. Deve conter:
Uma lista de estudantes (students).

Métodos para:
Adicionar um aluno: Valide que a idade e a série sejam números válidos.
Remover um aluno pelo ID.
Atualizar informações de um aluno: Atualize o nome, idade ou série pelo ID.
Listar todos os alunos, mostrando suas informações.
Buscar um aluno pelo nome e retornar suas informações.

Menu interativo (opcional):
O programa deve permitir o usuário escolher as opções acima de maneira simples.

Regras:
Não use frameworks ou bibliotecas externas.
Use apenas Python puro e, no máximo, bibliotecas da stdlib.
Foque na clareza, organização e boas práticas.


the series is base on 1 , 2 and 3 so  , age dosent matter the onyl thins is that    
it has to be above 18 and less than 50 
    1a , 1b , 1c
    2a , 2b , 2c
    3a , 3b , 3c

"""
import re 
from typing import *


class Student():
    def __init__(self, id:int , name:str , age:int , serie:str):
        self.id =id
        self.name =name
        self.age = age 
        self.serie = serie 
        
    def __str__(self):
        return f"id:{self.id} - Student:{self.name} - Age:{self.age} - Serie:{self.serie} "
    

ana = Student( 1 , "Ana" , 22 , "2a")
Erik = Student( 2 , "Erik" , 35 , "2c")
Gabriel = Student( 3 , "Gabriel" , 24 , "3c")
Luna = Student( 4 , "Luna" , 18 , "1a")
Lucas = Student( 5 , "Lucas" , 18 , "2a")

class Scholl():
    def __init__(self , name:str , students:list):
        self.name =name
        self.students = students
        
    """
        The functions bellow get valid data from user's input 
        to avoid bad data input's
        name can be only alphabetic letter's
        age can be only > 18 and <= 50
        serie can be only 1a , 1b , 1c / 2a , 2b , 2c / 3a , 3b , 3c
    """
    def generate_valid_id(self)->int:
        if self.students:
            return max(student.id for student in self.students) + 1


    def get_valid_id(self)->int:
        while True:
            try:
                valid_id = int((input("type sudent id : ")))
                if valid_id > 0 and valid_id <= len(self.students):
                    return valid_id
                else:
                    raise ValueError("Invalid ID")
            except ValueError as e :
                    print(f"Erro: {e} , please try again")
            except Exception as e :
                    print(f'Unexpected Erro:{e} , please try again')
                    break

    def get_valid_serie(self)->str:
            while True:
                try :
                    serie = str(input("Type the serie: "))
                    clean_serie = serie.strip().lower()
                    if len(clean_serie) == 2 and clean_serie[0] in "123" and clean_serie[1] in "abc":
                        return clean_serie
                    else:
                        raise ValueError("Invalid serie")
                except ValueError as e :
                    print(f"Erro: {e} , please try again")
                except Exception as e :
                    print(f'Unexpected Erro:{e} , please try again')
                    break
                    
    def get_valid_age(self)->int:
            while True:
                try :
                    age = int(input("Type the age: "))
                    if age >= 18 and age <= 50:
                        return age
                    else:
                        raise ValueError("Invalid age")
                except ValueError as e :
                    print(f"Erro: {e} , please try again")
                except Exception as e :
                    print(f'Unexpected Erro:{e} , please try again')
                    break
    
    def get_valid_name(self)->str:
            while True:
                try :
                    name = str(input("Student name: "))
                    if re.match(r'^[A-Za-z_]+$', name):
                        return name
                    else:
                        raise ValueError("Invalid age")
                except ValueError as e :
                    print(f"Erro: {e} , please try again")
                except Exception as e :
                    print(f'Unexpected Erro:{e} , please try again')
                    break
        
    """
        Functions bellow are the system funcionalaties
    """
    
    def list_all_students(self)->list:
        for student in self.students:
            print(student)

    def list_one_student(self)->list:
        search_id = self.get_valid_id()
        for student in self.students:
            if search_id == student.id:
                print(student)      
                
    def list_student_serie(self)->list:
        serie = self.get_valid_serie()
        print(f"Listing all students from {serie}")
        for student in self.students:
            if serie == student.serie:
                print(student)  
    
    def add_new_student(self)->None:
        student_id = self.generate_valid_id()
        name = self.get_valid_name()
        age = self.get_valid_age()
        serie = self.get_valid_serie()
        new_student = Student(student_id , name , age , serie)
        self.students.append(new_student)

    def remove_student(self)->None:
        remove_id = self.get_valid_id()
        for student in self.students:
            if student.id == remove_id:
                self.students.pop(remove_id-1)
                print(f"Student {student.name} from {student.serie} removed succefuly")

e = Scholl('escola' , [ana , Erik , Gabriel , Luna ,Lucas ])
e.list_all_students()
e.remove_student()
e.list_student_serie()

