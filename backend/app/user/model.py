from app.db import Entity, db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from .interface import PersonInterface, UserInterface
from werkzeug.security import generate_password_hash, check_password_hash

class Rol(Enum):
    ADMIN = 1
    FINANCIAL = 2
    CLIENT = 3
    @classmethod
    def get_index(cls, type):
        return list(cls).index(type)

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    person_id = Column(Integer, ForeignKey('persons.id'))

    person = relationship('Person')

    rol = Column(Integer, nullable=False)

    def update(self, changes: UserInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class Person(Entity, db.Model):
    __tablename__ = 'persons'
    
    name = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    last_name = Column(String(120), nullable=False)
    document = Column(String(8), nullable=False)

    def update(self, changes: PersonInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

    
