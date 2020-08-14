from app import db
from .model import Credit, RequestCredit
from .interface import CreditInterface, RequestCreditInterface
from typing import List

class CreditService:

    @staticmethod
    def get_all():
        return Credit.query.all()
    
    @staticmethod
    def get_by_id(id: int) -> Credit:
        return Credit.query.get(id)

    @staticmethod
    def update(credit: Credit, credit_change_updates: CreditInterface) -> Credit:
        credit.update(credit_change_updates)
        db.session.commit()
        return credit
    
    @staticmethod
    def create(new_attrs: CreditInterface) -> Credit:
        new_credit = Credit(
            amount=new_attrs["amount"], request_credit_id=new_attrs["request_credit_id"], answer_date=new_attrs["answer_date"],
            state=new_attrs["state"], user_id=new_attrs["user_id"], description=new_attrs["description"])

        db.session.add(new_credit)
        db.session.commit()
    
    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        credit = Credit.query.filter(Credit.id == id).first()
        if not credit:
            return []
        db.session.delete(credit)
        db.session.commit()
        return [id]
        
class RequestCreditService:
    
    @staticmethod
    def get_all():
        return RequestCredit.query.all()
    
    @staticmethod
    def get_by_id(id: int) -> RequestCredit:
        return RequestCredit.query.get(id)

    @staticmethod
    def update(request_credit: RequestCredit, request_credit_change_updates: RequestCreditInterface) -> RequestCredit:
        request_credit.update(request_credit_change_updates)
        db.session.commit()
        return request_credit
    
    @staticmethod
    def create(new_attrs: RequestCreditInterface) -> RequestCredit:
        new_request_credit = RequestCredit(
            amount=new_attrs["amount"], state=new_attrs["state"], user_id=new_attrs["user_id"])
        db.session.add(new_request_credit)
        db.session.commit()
    
    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        request_credit = RequestCredit.query.filter(RequestCredit.id == id).first()
        if not request_credit:
            return []
        db.session.delete(request_credit)
        db.session.commit()
        return [id]