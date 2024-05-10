from typing import Optional, Any

from pydantic import BaseModel, conint, EmailStr, constr, validator
from pydantic.main import Model


class User(BaseModel):
    username: str
    age: conint(gt=18)
    email: EmailStr
    password: constr(min_length=8, max_length=16)
    phone: Optional[str] = 'Unknown'

    @validator('username')
    @classmethod
    def validate_username(cls, value):
        if value == 'Adam':
            raise ValueError("Адам у нас только один может быть")
        return value
