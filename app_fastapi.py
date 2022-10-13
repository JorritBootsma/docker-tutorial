from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/hello/{name}")
def greet(name: str):
    return {"response": f"Hello {name}"}


@app.get("/goodbye/{name}")
def farewell(name: str):
    return {"response": f"Goodbye {name}!"}


@app.get("/test_with_latest")
def test():
    return {"response": "The latest image is pulled!"}


@app.get("/version_number")
def version_number():
    return {"response": "0.3.1-test_version_number"}
