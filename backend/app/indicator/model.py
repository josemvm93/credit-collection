from app.db import Entity, db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .interface import IndicatorInterface


class Indicator(Entity, db.Model):
    __tablename__ = 'indicators'

    name = Column(String(80), unique=True, nullable=False)    
    credit_id = Column(Integer, ForeignKey('credits.id'))

    value = Column(String(50), nullable=False)


    def update(self, changes: IndicatorInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
