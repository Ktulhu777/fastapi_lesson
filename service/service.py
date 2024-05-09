from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union
from models.models import Todo
from schema.schema import TodoSchemaUpdate


async def get_todo_list(session: AsyncSession, todo_id: int):
    result = await session.execute(select(Todo).filter_by(todo_id=todo_id))
    return result.scalars().all()


def add_todo(session: AsyncSession, todo_id: int,
             title: str, description: str, completed: bool):
    new_todo = Todo(todo_id=todo_id, title=title,
                    description=description, completed=completed)
    session.add(new_todo)
    return new_todo


async def update_todo(session: AsyncSession, todo: TodoSchemaUpdate, todo_id: int):
    todo_up = await session.execute(
        update(Todo)
        .where(Todo.todo_id == todo_id)
        .values(title=todo.title, completed=todo.completed)
    )
    return todo_up


async def read_todo(session: AsyncSession, todo_id: Union[int, None]):
    if todo_id is None:
        todo_read = await session.execute(select(Todo))
        return todo_read.scalars().all()
    todo_read = await session.execute(select(Todo).where(Todo.todo_id == todo_id))
    return todo_read.scalar_one_or_none()


async def delete_todo(session: AsyncSession, todo_id: int):
    todo = await session.execute(select(Todo).where(Todo.todo_id == todo_id))
    if todo.scalars().first():
        todo_delete = await session.execute(
            delete(Todo)
            .where(Todo.todo_id == todo_id)
            .returning(Todo.todo_id, Todo.title)
        )
        return todo_delete
    else:
        raise Exception
