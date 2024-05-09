from pydantic import BaseModel


class TodoSchemaCreate(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False


class TodoSchemaUpdate(BaseModel):
    title: str
    completed: bool = False
