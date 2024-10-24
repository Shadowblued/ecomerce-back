from pydantic import BaseModel

# Definindo a estrutura básica de um produto
class ProductBase(BaseModel):
    name: str # Nome do produto
    price: float # Preço do produto

# Modelo usado na criação de um novo produto
class ProductCreate(ProductBase):
    pass  # Não há novos campos além dos de ProductBase

# Modelo com o ID incluído, usado para leitura de dados
class Product(ProductBase):
    id: int # O ID é gerado automaticamente pelo banco de dados