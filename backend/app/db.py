from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
    
    # @classmethod
    # def get_all(cls):
    #     return cls.query.all()
    
    # @classmethod
    # def get_by_id(cls, id):
    #     return cls.query.get(id)