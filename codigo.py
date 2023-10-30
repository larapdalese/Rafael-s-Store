class produto:
    
    def __init__(self, bar_code, name, price, quantity):
        self.bar_code = bar_code
        self.name = name
        self.price = price
        self.quantity = quantity    

# =============================================================================================
class PRODUTO_Alimento(produto):
    def __init__(self, bar_code, name, price, quantity, validity):
        super().__init__(bar_code, name, price, quantity)
        self.validity = validity
    
    def print_infos(self):
        "Exibe o nome do produto e seu respectivo código de barras"
        return f"Código de barras: {self.bar_code} \nQuantidade: {self.quantity} \nNome: {self.name} \nPreço: {self.price} \nValidade: {self.validity} \n\n"

# =============================================================================================
class PRODUTO_Roupa(produto):
    def __init__(self, bar_code, name, price, quantity, size, color):
        super().__init__(bar_code, name, price, quantity)
        self.size = size
        self.color = color
    
    def print_infos(self):
        "Exibe o nome do produto e seu respectivo código de barras"
        return f"Código de barras: {self.bar_code} \nQuantidade: {self.quantity} \nNome: {self.name} \nPreço: {self.price} \nTamanho: {self.size} \nCor: {self.color} \n\n"

# ============================================================================================= 
class PRODUTO_Eletronico(produto):
    def __init__(self, bar_code, name, price, quantity, brand, color):
        super().__init__(bar_code, name, price, quantity)
        self.brand = brand
        self.color = color
        
    def print_infos(self):
        "Exibe o nome do produto e seu respectivo código de barras"
        return f"Código de barras: {self.bar_code} \nQuantidade: {self.quantity} \nNome: {self.name} \nPreço: {self.price} \nMarca: {self.brand} \nCor: {self.color}"


# ============================================================================================= 
class ERROS_DE_VENDAS(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        
# ============================================================================================= 
class Inventory:
    total_products_in_inventory = 0
    
    def __init__(self):
        self.products = []

    def register_prod(self, product):
        "Registra um novo produto ao inventário"
        
        # Erro
        for registered_product in self.products:
            if product.bar_code == registered_product.bar_code:
                raise ERROS_DE_VENDAS("Tentando registrar um produto que já está registrado no inventário")

        self.products.append(product)
        Inventory.total_products_in_inventory += 1
        
        return

    def delete_prod(self, bar_code):
        "Deleta um produto do inventário"
        indice = 0
        for product in self.products:
            if product.bar_code == bar_code:
                self.products.remove(product)
                Inventory.total_products_in_inventory -= 1
            else: indice += 1
            
        # Erro
        if indice == Inventory.total_products_in_inventory:
            raise ERROS_DE_VENDAS("Tentando deletar um produto que não está registrado no inventário")
     
        return
            
    def add_prod(self, bar_code, quantity):
        "Adiciona ao inventário a quantidade dada do produto correspondente ao código de barras"
        indice = 0
        for product in self.products:
            if product.bar_code == bar_code:
                product.quantity += quantity
                return
            else: indice += 1
        
        # Erro
        if indice == Inventory.total_products_in_inventory:
            raise ERROS_DE_VENDAS("Tentando adicionar um produto que não está registrado no inventário")
        
        return
            
    def rem_prod(self, bar_code, quantity):
        "Remove do inventário a quantidade dada do produto correspondente ao código de barras"
        for product in self.products:
            if product.bar_code == bar_code:
                product.quantity -= quantity    
                
        # Erro
        if product.quantity < 0:
            raise ERROS_DE_VENDAS("Não há quantidades suficientes do produto no estoque")

        return
            
    def print_inv(self):
        if Inventory.total_products_in_inventory == 0:
            raise ERROS_DE_VENDAS("O Inventário está vazio")
        
        "Exibe as informações dos produtos do inventário"
        resultado = "Inventário:\n\n"
        for produto in self.products:
            resultado += produto.print_infos()
        return resultado
    