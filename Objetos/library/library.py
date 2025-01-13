"""
Exercício: Sistema de Gerenciamento de Biblioteca
Objetivo: Criar um sistema para gerenciar uma biblioteca. Você utilizará classes para 
representar livros e a biblioteca, e implementará funcionalidades como 
adicionar, remover, pesquisar e listar livros.

Requisitos:

Classe Livro:
Atributos:
Título (string)
Autor (string)
ISBN (string)
Disponibilidade (boolean)
Métodos:
__str__: para retornar uma representação legível do livro.

Classe Biblioteca:
Atributos:
Uma lista de livros.
Métodos:
adicionar_livro: Adiciona um novo livro à biblioteca.
remover_livro: Remove um livro da biblioteca pelo id.
pesquisar_livro: Busca um livro  exibe suas informações.
listar_livros: Exibe todos os livros disponíveis na biblioteca.
emprestar_livro: Altera a disponibilidade de um livro para False (indica que foi emprestado).
devolver_livro: Altera a disponibilidade de um livro para True (indica que foi devolvido).

Desafios Adicionais:

Implemente a funcionalidade de listar apenas os livros disponíveis.

Adicione tratamento de erros para entradas inválidas (por exemplo, ISBN não encontrado).


Dicas:
Pense na estrutura de dados que melhor se adapta para armazenar os livros.
Utilize métodos de classe para manter a lógica clara e organizada.
Teste cada funcionalidade à medida que a implementa.
Quando terminar, compartilhe seu código e posso dar feedback! Boa sorte!

"""
from typing import *

class Book:
    def __init__(self , title:str ,author:str, id:int , avalible=True)-> None :
        self.title = title
        self.author = author 
        self.id = id
        self.avalible = avalible
        
    def __str__(self) -> str:
        return f"title: {self.title} made my {self.author}"
    
Celest = Book("Celest" , "Yuha" , 1)
Berserk = Book("Berserk" , "Miamura" , 2)
    
class Library():
    def __init__(self, name:str )-> None :
        self.name = name 
        self.books : Dict[object:Book] ={
            "Celest":Celest,
            "Berserk":Berserk,
        }
        
    def __str__(self)-> str:
        return f"library name {self.name}"
    
    #Validate functions are bellow
    def _find_book(self, book:str=0) -> bool:
        #Return True  if book is found
        """is Working proprely"""
        return book in self.books

    def _find_id(self, id: int=0) -> int:
        """Find an existing book ID."""
        while True:
            try:
                book_id = int(input("Find ID: "))
                for value in self.books.values():
                    if value.id == book_id:
                        return book_id
                print("ID not found. Please try again.") 
            except ValueError:
                print("Invalid value typed. Please enter a number.")


    def _create_valid_book_id(self)->int:
        # get a valid id 
        """Is working proprely"""
        while True:
            try:
                book_id = int(input("Book ID: "))
                for value in self.books.values():
                    if value.id == book_id:
                        print("ID already exists, please enter a different ID.")
                        break
                print("ID is valid")
                return book_id
            except ValueError:
                print("Invalid value typed. Please enter a number.")

    #CRUD operations are bellow 
    
    def add_book(self , book:object=None):
        #Create a book
        """ we cant validade title nor author , the can start with numbers"""
        print("Lest create a book")
        title = str(input("title: "))
        author = str(input("author: "))
        id = self._create_valid_book_id()
        book = Book(title , author , id)
        self.books[title]=book
        print("Book created")
    
    def remove_book(self, book_id=0)-> None:
        #Remove a book by id
        """OK"""
        print("Lest remove a book")
        book_id = self._find_id()
        for key , value in list(self.books.items()):
            if book_id == value.id:
                del self.books[key]
                print("Book successfully deleted")
                break
    
    def read_one_book(self, id:int=0)->None:
        #read one book 
        """could be better? in dont know"""
        print("Lets search for a book")
        self._find_id()
        
    def read_all_books(self)-> None:
        #Read all books
        "ok"
        print("Listing all books")
        for book in self.books.values():
            print(book)
            
    def borrow_book(self, id:int=0)->None:
        ("Borring a book")
        book_id = self._find_id()
        for value in self.books.values():
            if book_id == value.id:
                value.avalible = False
                print(f"Book borrwed") 
                
    def ledn_back_book(self):
        print("Returning a book")
        book_id = self._find_id()
        for value in self.books.values():
            if book_id == value.id:
                value.avalible = True
                print(f"Book returned") 
        



library = Library("lib")
print(library._find_book("Celest"))
library.add_book()
library.remove_book()
library.read_one_book()
library.read_all_books()
library.borrow_book()


