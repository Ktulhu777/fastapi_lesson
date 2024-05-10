from fastapi import FastAPI
from starlette.responses import JSONResponse

from exception.exception import CustomException
from schema.schema import User

app = FastAPI()


@app.exception_handler(CustomException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


@app.post('/registration/')
async def get_registration(user: User):
    try:
        return user
    except Exception as e:
        print(e)
        return "Юзер не был создан"
