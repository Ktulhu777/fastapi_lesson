from fastapi import FastAPI, HTTPException
from schema.schema import User
from fastapi import status

app = FastAPI()

users = [{"username": "Adam", "email": "exampl@mail.com", "password_1": "123456789", "password_2": "123456789"},
         {"username": "DC", "email": "exampl@mail.com", "password_1": "123456789", "password_2": "123456789"},
         {"username": "Vova", "email": "exampl@mail.com", "password_1": "123456789", "password_2": "123456789"}]


@app.post("/registration/", status_code=status.HTTP_201_CREATED)
async def registration_user(user: User):
    try:
        if user.password_1 != user.password_2:
            raise ValueError

        return {"success": "Пользователь создан",
                "user": user}
    except ValueError:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Пароли не совпадают")


@app.get("/user/{username}/")
async def get_user(username: str):
    user_found = None
    for item in users:
        if username == item['username']:
            user_found = item
            break

    if user_found is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user_found


@app.delete("/del_user/{username}/")
async def del_user(username: str):
    user_found = None
    for item in users:
        if username == item['username']:
            user_found = item
            break

    if user_found is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return {"delete": "User del",
            "user": user_found}
