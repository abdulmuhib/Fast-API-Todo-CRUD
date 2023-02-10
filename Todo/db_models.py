from sqlalchemy import Column, Integer, String
from base import Base


class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
