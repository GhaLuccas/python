"""
Desafio: Análise Simples de Dados de Vendas

Enunciado: Desenvolva um pequeno programa em Python que analise dados de vendas de uma loja. 
O programa deve ser capaz de ler os dados de vendas de uma lista de dicionários 
e responder a perguntas básicas sobre os dados.

Especificações do exercício:

Dados de entrada:

Um conjunto de dados de vendas em formato de lista de dicionários. 
Cada dicionário representa uma venda 
e contém as seguintes chaves: produto, quantidade e preco_unitario. Exemplo:

exeplo
vendas = [
    {"produto": "Camiseta", "quantidade": 2, "preco_unitario": 50.0},
    {"produto": "Calça", "quantidade": 1, "preco_unitario": 120.0},
    {"produto": "Meias", "quantidade": 5, "preco_unitario": 10.0},
    # Mais itens...
]

Requisitos:

1.Implemente uma função que calcule o total de vendas (quantidade × preço unitário para cada item).

2.Crie uma função que encontre o produto mais vendido em termos de quantidade.

3.Implemente uma função que calcule a média do valor total das vendas.

Desafios adicionais (opcional):
1.Adicione uma função que mostre o total de vendas por produto.

2.Implemente uma forma de exibir os produtos ordenados pelo valor total de vendas.

Regras:
Utilize apenas Python puro e bibliotecas padrão (como math se precisar de funções matemáticas).
Documente cada função explicando seu propósito e os parâmetros que recebe.

"""
from typing import *
import random

# Example products
products = [
    "Camiseta", "Calça", "Meias", "Tênis", "Jaqueta", "Blusa", "Vestido", "Saia", "Casaco", "Shorts",
    "Macacão", "Bermuda", "Bota", "Sapatilha", "Tênis", "Chapéu", "Relógio", "Bolsa", "Carteira", "Óculos"
]

# Function to generate the data
def generate_data(num_items=10):
    data = []
    for _ in range(num_items):
        product = random.choice(products)
        quantity = random.randint(1, 20)
        unit_price = round(random.uniform(1.0, 100.0), 2)
        data.append({"product": product, "quantity": quantity, "unitay_price": unit_price})
    return data

data = generate_data()
data1 = [
    {"product": "Camiseta", "quantity": 7, "unitay_price": 50.0},
    {"product": "Calça", "quantity": 1, "unitay_price": 120.0},
    {"product": "Meias", "quantity": 4, "unitay_price": 10.0},
    {"product": "socktes", "quantity": 7, "unitay_price": 10.0},
    {"product": "minha", "quantity": 5, "unitay_price": 10.0},
]

class Sales_analizer:
    def __init__(self ,data:list):
        self.sales = data
        
    def __str__(self):
        return 'Sales Analizer'
    
    def total_purchases_value(self)-> float:
        # use the data to calcule total valor 
        total = 0.0
        for dict in self.sales:
                quantity  = dict["quantity"] 
                unitay_price = dict['unitay_price']

                total+= quantity*unitay_price
        return total
    
    def per_purchase_total_price(self)-> list:
        per_list =[]
        for dict in self.sales:
            per_list.append(dict['quantity'] * dict['unitay_price'])
        return per_list
    
    def diplay_per_list_price(self)->str:
        lista = self.per_purchase_total_price()
        for n in range(len(lista)):
            print(f"The purchase number {n+1} had a price of R${lista[n]:.2f}")
        
        
    def most_quantity(self)->dict:
        # loop's trow qte's to see the biggest one
        itens = []
        values = []
        data = {"item":itens , "quantity":0}
        for dict in self.sales:
            if  dict['quantity'] >= data["quantity"]:
                values.append(dict['quantity'])
            if dict['quantity'] == max(values):
                itens.append(dict['product'])
                data['quantity'] = max(values)
        return data
        
    def purchases_avarege_price(self)->float:
        # gets the avarege purchases prices 
        total = self.total_purchases_value()
        media = total / len(self.sales)
        return media
        


analiser = Sales_analizer(data1)
total = analiser.total_purchases_value()
mostQte = analiser.most_quantity()
avaragePrice = analiser.purchases_avarege_price()


analiser.diplay_per_list_price()
print(f"The item who sold the most quantaty was {mostQte} ")
print(f"The avarage money spend in purchases is R${avaragePrice:.2f}")
print(f"The total price os the purchases is: R${total:.2f} ")


