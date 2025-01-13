"""
Exercício: Sistema de Gerenciamento de Inventário de Loja
Enunciado: Crie um programa em Python que gerencie o inventário de uma loja. 
O sistema deve permitir que o usuário adicione, remova e atualize produtos, 
além de realizar buscas e exibir o inventário completo.

Especificações do exercício:
Dados do produto: Cada produto deve ter as seguintes informações:

ID (único e gerado automaticamente)
Nome
Quantidade em estoque
Preço unitário

Funcionalidades:
1- Adicionar um novo produto ao inventário.
2- Remover um produto pelo ID.
3- Atualizar a quantidade ou o preço de um produto existente.
4- Buscar produtos por nome (retornar produtos que contêm o termo de busca).
5- Exibir o inventário completo em um formato tabular.

Desafios adicionais (opcional):
Implemente uma função que permita ordenar o inventário por nome, quantidade ou preço.
Adicione uma funcionalidade para exportar o inventário completo para um arquivo CSV.
Inclua uma função de importação que leia dados de um arquivo CSV e os adicione ao inventário.

Regras:
Utilize apenas Python puro e bibliotecas padrão (como csv e tabulate).
Comente o código para facilitar a compreensão.

Exemplo de uso: O programa deve apresentar um menu com opções como:
Adicionar produto
Remover produto
Atualizar produto
Buscar produto
Exibir inventário
Sair

Quando o usuário seleciona uma opção, a funcionalidade correspondente é executada.
Boa sorte! Este exercício é ideal para treinar manipulação de listas e dicionários, 
além de trabalhar com funções e lógica de programação. Se precisar de alguma dica ou 
ajuda com a implementação, fique à vontade para perguntar!

"""

from typing import *

class Product():
    def __init__(self , id:int , name:str , quantity:int , unitary_price:float):
        self.id = id 
        self.name = name 
        self.unitary_price = unitary_price
        self.quantity = quantity 

    
    def __str__(self)-> str:
        return f'id:{self.id} - Product:{self.name} - Price:{self.unitary_price} - Quantity:{self.quantity}'
    
    
test_item1 = Product(1, 'item1' , 10.0 ,1 )
test_item2 = Product(2, 'item2' , 20.0 ,2 )
    
class Inventory():
    def __init__(self , name:str , stock:list):
        self.name = name 
        self.stock = stock

    
    def __str__(self):
        pass
    
    def list_all_item(self)-> None:
        """List all itens in the stock even 0 """
        for item in self.stock:
            for name , info  in item.items():
                print(info)
    
    
    def add_new_product(self)-> None:
        """
        create and add a new product dosen't need to verify if item already exist  
        Itens can have the same name and names can be numbers like '12 chocolate'
        
        """
        
        new_item_id = len(self.stock) + 1
        while True:
            try:
                new_item_name = input("Type the new product name: ").strip()
                new_item_price = float(input("Type the new product price: "))
                new_item_quantity = int(input("Type the new product quantity: "))
                
                if new_item_quantity < 0 or new_item_price < 0:
                    raise ValueError("Price and quantity must be positive numbers.")
                
                new_item = Product(
                    id = new_item_id , 
                    name = new_item_name , 
                    unitary_price = new_item_price , 
                    quantity = new_item_quantity
                    )
                
                item_data = {new_item_name: new_item}
                self.stock.append(item_data)
        
                print("Item created sucessfully!")
                break
            
            except ValueError as e:
                print(f"Error: {e}. Please Try again.")
            except Exception as e:
                print(f"Unexpected error: {e}. Operation canceled.")
                break
                
            
    def remove_item(self):
        """
        remove and item looping through all the items searching by id 
        
        """
        while True:
            try:
                item_id = int(input("Type the ID of the item to remove: "))
                if item_id <= 0 or item_id > len(self.stock):
                    raise ValueError("ID invalid")
                for item in self.stock:
                    for name , info in item.items():
                        if info.id == item_id:
                            print('sucessufully removed item',info)
                            self.stock.pop(info.id -1 )
                break
            except ValueError as e :
                print(f"Erro : {e}. Please try again.")
            except Exception as e :
                print(f"Unexpected error : {e}. Operation canceled")
                
    def update_item(self):
        """
        update existem item by id 
        
        """
        while True:
            try:
                item_id = int(input("Type the ID of the item to remove: "))
                if item_id <= 0 or item_id > len(self.stock):
                    raise ValueError("ID invalid")
                for item in self.stock:
                    for name , info in item.items():
                        if info.id == item_id:
                            print("Item found")
                            try:
                                udate_name = input("Type the new product name: ").strip()
                                udate_item_price = float(input("Type the new product price: "))
                                udate_item_quantity = int(input("Type the new product quantity: "))
                                if item_id <= 0 or item_id > len(self.stock):
                                    raise ValueError("ID invalid")
                            except ValueError as e :
                                print(f"Erro : {e}. Please try again.")
                            except Exception as e :
                                print(f"Unexpected error : {e}. Operation canceled")
                break
            except ValueError as e :
                print(f"Erro : {e}. Please try again.")
            except Exception as e :
                print(f"Unexpected error : {e}. Operation canceled")
                
        

invet = Inventory("invent", [])
invet.add_new_product()
invet.add_new_product()
invet.list_all_item()
invet.remove_item()
invet.list_all_item()
