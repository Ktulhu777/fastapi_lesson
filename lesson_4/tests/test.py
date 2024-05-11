from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_calculate_sum():
    response = client.get("/sum/?a=5&b=10")
    assert response.status_code == 200
    assert response.json() == {"result": 15}


def test_creation_user():
    response = client.post(
        "/registration/?username='Adam'&email='user@example.com'&password_1='string'&password_2='string'"
    )
    assert response.status_code == 200
    assert response.json() == {
        "username": "string",
        "email": "user@example.com",
        "password_1": "stfdfdsfds",
        "password_2": "string"
    }

    response_2 = client.post(
        "/registration/?username='Adam'&email='user@example.com'&password_1='strfsdfsdng'&password_2='string'"
    )
    assert response_2.status_code == 400
    assert response_2.json() == {
        "status_code": 400,
        "detail": "Пароли не совпадают",
        "headers": None
    }


def test_delete_user():
    response = client.delete('/del_user/1/')
    assert response.status_code == 200


# {
#     "status_code": 404,
#     "detail": "User not found",
#     "headers": None
# }
