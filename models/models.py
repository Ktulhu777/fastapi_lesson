from sqlalchemy import Column, String, Integer, Boolean, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todo"

    todo_id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text, nullable=False)
    completed = Column(Boolean, default=False)
