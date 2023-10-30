class produto:
    def __init__(self, bar_code, name, price, quantity):
        self.bar_code = bar_code
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_bar_code(self):
        "Exibe o nome do produto e seu respectivo código de barras"
        return f"{self.name} -> Bar code: {self.bar_code}."
    
    
# =============================================================================================
class prod_Tipo1(produto):
    def __init__(self, bar_code, name, price, quantity):
        super().__init__(bar_code, name, price, quantity)
    
# =============================================================================================
class prod_Tipo2(produto):
    def __init__(self, bar_code, name, price, quantity):
        super().__init__(bar_code, name, price, quantity)
        
    
# ============================================================================================= 
class prod_Tipo3(produto):
    def __init__(self, bar_code, name, price, quantity):
        super().__init__(bar_code, name, price, quantity)
        
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
        "Remove do inventário a quantidade dada do produto correspondente ao código de barras"
        for product in self.products:
            if product.bar_code == bar_code:
                product.quantity -= quantity
                return

    def print_inv(self):
        "Exibe as informações dos produtos do inventário"
        resultado = "\nInventário:\n"
        for product in self.products:
            resultado += f"\nProduct: {product.bar_code} - {product.name} - {product.price}\nQuantity: {product.quantity}\n"
        return resultado
