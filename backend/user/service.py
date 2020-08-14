from app import db
from .model import User, Person
from .interface import UserInterface, PersonInterface
from typing import List

class UserService:

    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id: int) -> User:
        return User.query.get(id)

    @staticmethod
    def update(user: User, user_change_updates: UserInterface) -> User:
        user.update(user_change_updates)
        db.session.commit()
        return user
    
    @staticmethod
    def create(new_attrs: UserInterface) -> User:
        new_user = User(username=new_attrs["username"], password=new_attrs["password"], person_id=new_attrs["person_id"], rol=new_attrs["rol"])

        db.session.add(new_user)
        db.session.commit()
    
    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        user = User.query.filter(User.id == id).first()
        if not user:
            return []
        db.session.delete(user)
        db.session.commit()
        return [id]
        
class PersonService:
    
    @staticmethod
    def get_all():
        return Person.query.all()
    
    @staticmethod
    def get_by_id(id: int) -> Person:
        return Person.query.get(id)

    @staticmethod
    def update(person: Person, person_change_updates: PersonInterface) -> Person:
        person.update(person_change_updates)
        db.session.commit()
        return person
    
    @staticmethod
    def create(new_attrs: PersonInterface) -> Person:
        new_person = Person(email=new_attrs["email"], name=new_attrs["name"], last_name=new_attrs["last_name"], document=new_attrs["document"])

        db.session.add(new_person)
        db.session.commit()
    
    @staticmethod
    def delete_by_id(id: int) -> List[int]:
        person = Person.query.filter(Person.id == id).first()
        if not person:
            return []
        db.session.delete(person)
        db.session.commit()
        return [id]