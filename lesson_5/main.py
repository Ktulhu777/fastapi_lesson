from fastapi import FastAPI, Request
from pydantic import BaseModel

from api_v1 import api_v1_app
from electronics import electronicsroute
from gadgets import gadgetsroute


def start():
    print("Приложение начало работу!")


def end():
    print("Приложение завершила работу")


app = FastAPI(on_startup=[start], on_shutdown=[end])
app.mount('/v1/', api_v1_app)  # суб-приложение
app.include_router(electronicsroute, prefix="/electronics")  # http://localhost:8000/electronics/info и
app.include_router(gadgetsroute,
                   prefix="/gadgets")  # http://localhost:8000/gadgets/info


@app.middleware("http")  # что то выполняет до функии ну после нее
async def my_middleware(request: Request, call_next):
    print('Мидлвэр начал работу')
    response = await call_next(request)
    print('Мидлвэр получил обратно управление')
    return response


@app.get("/")
def index():
    print('привет из основного обработчика пути')
    return {"message": "Hello, world!"}


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
