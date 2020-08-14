from app import db
from .model import Indicator
from .interface import IndicatorInterface
from typing import List

class IndicatorService:

    @staticmethod
    def get_all():
        return Indicator.query.all()
    
    @staticmethod
    def get_by_id(id: int) -> Indicator:
        return Indicator.query.get(id)

    @staticmethod
    def update(indicator: Indicator, indicator_change_updates: IndicatorInterface) -> Indicator:
        indicator.update(indicator_change_updates)
        db.session.commit()
        return indicator
    
    @staticmethod
    def create(new_attrs: IndicatorInterface) -> Indicator:
        new_indicator = Indicator(name=new_attrs["name"], credit_id=new_attrs["credit_id"], value=new_attrs["value"])

        db.session.add(new_indicator)
        db.session.commit()
    
    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        indicator = Indicator.query.filter(Indicator.id == id).first()
        if not indicator:
            return []
        db.session.delete(indicator)
        db.session.commit()
        return [id]
        