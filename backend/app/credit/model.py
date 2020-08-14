from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from enum import Enum
from .interface import CreditInterface, RequestCreditInterface
from app.db import Entity, db

class CreditState(Enum):
    APPROVED = 1
    ON_HOLD = 2
    REJECTED = 3

class RequestCreditState(Enum):
    CREATED = 1,
    ON_HOLD = 2,
    FINALIZED = 3


# class Credit(Entity, Base):
class Credit(Entity, db.Model):
    __tablename__ = 'credits'

    amount = Column(Integer, nullable=False)
    request_credit_id = Column(Integer, ForeignKey('request_credits.id'))
    answer_date = Column(DateTime)
    state = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    description = Column(String(300), nullable=False)

    user = relationship('User')
    indicators = relationship('Indicator', backref='credits', lazy=True)

    def update(self, changes: CreditInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

class RequestCredit(Entity, db.Model):
    __tablename__ = 'request_credits'

    amount = Column(Integer, nullable=False)
    state = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User')

    def update(self, changes: RequestCreditInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self