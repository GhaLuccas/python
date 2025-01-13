"""
Exercício: Sistema de Controle de Estoque

Objetivo: Criar um sistema simples para gerenciar o estoque de produtos 
de uma loja. Você vai utilizar classes para representar produtos e o estoque
, e deve implementar funcionalidades como 
adicionar, remover e atualizar a quantidade de produtos no estoque.

Requisitos:

Classe Produto:
A classe Produto deve conter:
Nome do produto (string)
Preço (float)
Quantidade disponível (inteiro)

Classe Estoque:
A classe Estoque deve ter uma 
lista de produtos e os seguintes métodos:

1-adicionar_produto: Adiciona um novo produto ao estoque.

2-remover_produto: Remove um produto do estoque pelo nome.

3-atualizar_quantidade: Atualiza a quantidade de um produto no estoque.

4-mostrar_estoque: Exibe a lista de produtos no estoque com suas respectivas 
quantidades e preços.

5- buscar_produto: Busca um produto pelo nome e exibe suas informações.

Regras:
O produto só pode ser adicionado se ainda não estiver no estoque.
A quantidade de um produto só pode ser atualizada se ele já estiver 
no estoque.
Não é possível remover um produto que não está no estoque.

Desafio adicional:
Adicione uma função que calcule o valor total do estoque, ou seja, a 
soma do preço de todos os produtos multiplicados pelas suas respectivas 
quantidades.

"""

class Product:
    def __init__(self , name , price , quant):
        self.name = name
        self.price = price 
        self.quant = quant
    def __str__(self):
        return self.name
    
laptop = Product("laptop" , 4000.00 , 5)
cellphone = Product("cellphone" , 2100.00 , 25)

class Stok:
    def __init__(self , name):
        self.name=name
        self.products = {
            "laptop" : laptop
        }   
    
    def __str__(self):
        return self.name
    
    #Plural CRUD operations
    def list_all(self):
        for k , v in self.products.items():
            print(f"item:{k} - preço: {v.price} - quantity:{v.quant}")
    
    def sum_all_products(self):
        total = 0 
        for k ,v in self.products.items():
            total += v.price * v.quant
        return total
    
    # Singular CRUD operations 
    def add_product(self):
        try:
            name = str(input("type name: "))
            if name not in self.products:
                    price = float(input("type price: "))
                    quant = int(input("type quantity: "))
                    product = Product(name , price , quant)
                    self.products[name]=product
            else:
                    print("This product is alredy registered")
        except ValueError:
            print("Valor invalido",ValueError)

    def remove_product(self):
        keys_to_delet =[]
        try:
            key_to_remove =str(input("Item to delete: "))
            if key_to_remove in self.products:
                #Here we add the itens we want to remove in a list
                #and then we delet them afther de itiration
                for k in list(self.products.keys()):
                    if k == key_to_remove:
                        keys_to_delet.append(k)
                for key in keys_to_delet:
                    del self.products[key]
            else:
                print("product not found")
        except TypeError:
            print(TypeError)
    
    def update_item_quantity(self):
        try:
            item = str(input("Item to update: "))
            if item in self.products:
                new_quant = self._get_int_input()
                self.products[item].quant = new_quant
            else:
                print("item not found")
        except ValueError as erro:
            print(erro)

    def list_one(self):
        name = input("Produto a buscar: ")
        product = self.products.get(name)
        if product:
            print(product)
        else:
            print("Produto não encontrado.")
            
            
            

    def _get_int_input(self, prompt):   
        """Obtém uma entrada válida do usuário como int."""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Por favor, insira um número válido.")
                

#tests
stok = Stok("stok")
stok.add_product()
    
        
    
    