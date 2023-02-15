from fastapi import FastAPI
from src.interface.controllers import items_controller

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(items_controller.router)