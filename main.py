from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config import DB_PASS, DB_NAME, DB_USER, DB_HOST
from service import service
from schema.schema import TodoSchemaCreate, TodoSchemaUpdate

app = FastAPI()
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@app.get('/todo/', status_code=200)
async def get_todo_list(session: AsyncSession = Depends(get_session),
                        todo_id: int = None):
    todo_read = await service.read_todo(session=session, todo_id=todo_id)
    try:
        return todo_read
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=404, detail="User not found")


@app.post('/todo/', status_code=201)
async def create_todo_list(todo: TodoSchemaCreate, session: AsyncSession = Depends(get_session)):
    todo_create = service.add_todo(session, todo.id, todo.title,
                                   todo.description, todo.completed)
    try:
        await session.commit()
        await session.refresh(todo_create)
        return {'detail': "Данные успешно добавлены"}
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail="Failed to create user")


@app.put('/todo/', status_code=200)
async def put_todo(todo_id: int, todo: TodoSchemaUpdate, session: AsyncSession = Depends(get_session)):
    await service.update_todo(session=session, todo=todo, todo_id=todo_id)

    try:
        await session.commit()
        return {'detail': "Данные успешно обновлены"}
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail="User now update")


@app.delete('/todo/', status_code=200)
async def del_todo(todo_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await service.delete_todo(session=session, todo_id=todo_id)
        await session.commit()
        return {'detail': 'Заметка удалена'}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Not delete")
