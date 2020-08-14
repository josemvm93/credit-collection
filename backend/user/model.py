from app.db import Base, Entity
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from .interface import PersonInterface, UserInterface

class Rol(Enum):
    ADMIN = 1
    FINANCIAL = 2
    CLIENT = 3

class User(Entity, Base):
    __tablename__ = 'users'

    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(30), nullable=False)

    person_id = Column(Integer, ForeignKey('persons.id'))

    person = relationship('Person')

    rol = Column(Integer, nullable=False)

    def update(self, changes: UserInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self


class Person(Entity, Base):
    __tablename__ = 'persons'
    
    name = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    last_name = Column(String(120), nullable=False)
    document = Column(String(8), nullable=False)

    def update(self, changes: PersonInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

    
