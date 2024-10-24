from fastapi import APIRouter, HTTPException
from app.services.product_service import ProductService
from app.models.product_model import Product, ProductCreate

router = APIRouter()
service = ProductService()

@router.get("/product", response_model=list[Product])
def get_all_products():
    return service.get_all_products()

@router.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    product = service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/save", response_model=Product)
def create_product(product: ProductCreate):
    return service.create_product(product)

@router.delete("/products/delete/{product_id}")
def delete_product(product_id: int):
    deleted = service.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}