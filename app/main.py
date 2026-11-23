
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Catalog Service",
    description="Sample product catalog microservice",
    version="1.0.0",
)

products = [
    {"id": 1, "name": "Laptop", "price": 1200.00},
    {"id": 2, "name": "Keyboard", "price": 75.00},
    {"id": 3, "name": "Mouse", "price": 35.00},
]


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")
