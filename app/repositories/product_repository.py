from app.models.product_model import ProductCreate
from typing import List

# Simulação de um banco de dados em memória
class ProductRepository:
    def __init__(self):
        # Simulação de dados
        self.products = [] # Lista que armazenará os produtos
        self.current_id = 1 # ID único para cada produto

    def get_all_products(self) -> List[dict]:
        return self.products

    def get_product_by_id(self, product_id: int) -> dict:
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def create_product(self, product: ProductCreate) -> dict:
        new_product = {
            "id": self.current_id,
            "name": product.name,
            "price": product.price
        }
        self.products.append(new_product)
        self.current_id += 1
        return new_product

    def delete_product(self, product_id: int) -> bool:
        for product in self.products:
            if product['id'] == product_id:
                self.products.remove(product)
                return True
        return False