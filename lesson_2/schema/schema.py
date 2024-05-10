from pydantic import BaseModel


class CustomExceptionModel(BaseModel):
    status_code: int
    er_message: str
