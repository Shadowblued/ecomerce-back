from fastapi import FastAPI
from app.controllers.product_controller import router as product_router

import uvicorn

app = FastAPI()
app.include_router(product_router)

@app.get("/")
def produtos():
    return {"produtos" : "todos"}

@app.get("/")

def read_root():

    return {"Hello": "World"}
def main():

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":

    main()