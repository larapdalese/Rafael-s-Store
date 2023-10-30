class produto:
    def __init__(self, name, bar_code, quantity):
        self.name = name
        self.bar_code = bar_code
        self.quantity = quantity
    
    def get_bar_code(self):
        "Exibe o nome do produto e seu respectivo código de barras"
        return f"{self.name} -> Bar code: {self.bar_code}."
    
    
# =============================================================================================
class prod1(produto):
    def __init__(self, name, bar_code, quantity):
        super().__init__(name, bar_code, quantity)
    
# =============================================================================================
class prod2(produto):
    def __init__(self, name, bar_code, quantity):
        super().__init__(name, bar_code, quantity)
        
    
# ============================================================================================= 
class prod3(produto):
    def __init__(self, name, bar_code, quantity):
        super().__init__(name, bar_code, quantity)
        
# ============================================================================================= 

class Inventory:
    def __init__(self):
        self.products = []

    def register_prod(self, product):
        "Registra um novo produto ao inventário"
        self.products.append(product)

    def delete_prod(self, bar_code):
        "Deleta um produto do inventário"
        for product in self.products:
            if product.bar_code == bar_code:
                self.products.remove(product)
                return
            
    def add_prod(self, bar_code, quantity):
        "Adiciona ao inventário a quantidade dada do produto correspondente ao código de barras"
        for product in self.products:
            if product.bar_code == bar_code:
                product.quantity += quantity
                return
            
    def rem_prod(self, bar_code, quantity):
        "Adiciona ao inventário a quantidade dada do produto correspondente ao código de barras"
        for product in self.products:
            if product.bar_code == bar_code:
                product.quantity -= quantity
                return

    def print_inv(self):
        "Exibe as informações dos produtos do inventário"
        resultado = "\nInventário:\n"
        for product in self.products:
            resultado += f"\nBar code: {product.bar_code}\nName: {product.name}\nQuantity: {product.quantity}\n"
        return resultado

    
# ============================================================================================= 
# Teste

# Criando produtos
produto_1 = prod1("Chocolate", 111111, 0)
produto_2 = prod2("Refrigerante", 222222, 0)
produto_3 = prod3("Cereal", 333333, 0)

print(produto_1.get_bar_code())
print(produto_2.get_bar_code())
print(produto_3.get_bar_code())

print("-"*10)

# Criando inventário
inventario = Inventory()

# Registrando os produtos ao inventário
inventario.register_prod(produto_1)
inventario.register_prod(produto_2)
inventario.register_prod(produto_3)

print(inventario.print_inv())

print("-"*10)

# Adicionando quantidades de produtos ao inventário
inventario.add_prod(111111, 1)
inventario.add_prod(222222, 2)
inventario.add_prod(333333, 3)

print(inventario.print_inv())

print("-"*10)

# Removendo quantidades de produtos ao inventário
inventario.rem_prod(111111, 0)
inventario.rem_prod(222222, 1)
inventario.rem_prod(333333, 2)

print(inventario.print_inv())













