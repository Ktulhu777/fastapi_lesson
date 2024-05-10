import uvicorn
from fastapi import FastAPI, Request
from starlette import status
from fastapi.responses import JSONResponse

from schema.schema import CustomExceptionModel
from exception.exception import CustomExceptionA, CustomExceptionB

app = FastAPI()


@app.exception_handler(CustomExceptionA)
async def custom_exception_handler(request: Request, exc: CustomExceptionB):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


@app.exception_handler(CustomExceptionB)
async def custom_exception_handler(request: Request, exc: CustomExceptionB):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


@app.get('/item/{item_id}', response_model=None)
async def get_item(item_id: int):
    if item_id == 9:
        raise CustomExceptionA(detail="Неприавильное число", status_code=status.HTTP_400_BAD_REQUEST)
    return CustomExceptionModel(status_code=200, er_message=f"Вот ваше число {item_id}")


@app.get('/item/{name}', response_model=None)
async def get_name(name: str):
    if name == "john":
        raise CustomExceptionB(detail="Неприавильное Имя", status_code=status.HTTP_400_BAD_REQUEST)
    return CustomExceptionModel(status_code=200, er_message=f"Вот имя {name}")


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
