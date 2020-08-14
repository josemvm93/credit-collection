from datetime import datetime
from flask_script import Command

from app.db import db
from app.user import Person, User, Rol

def seed_persons_users():
    ids = []
    for i in range(5):
        person = Person('test')
        person.name = "person" + str(i)
        person.last_name = "last" + str(i)+ "name"
        person.email = "person" + str(i)+ "@gmail.com"
        person.document = "12345678"
        db.session.add(person)
        db.session.commit()
        ids.append(person.id)
    
    user1 = User("test")
    user1.username = "financial@gmail.com"
    user1.set_password("financial")
    user1.rol = Rol.get_index(Rol.FINANCIAL)
    user1.person_id = ids[0]
    db.session.add(user1)

    user2 = User("test")
    user2.username = "admin@gmail.com"
    user2.set_password("admin")
    user2.rol = Rol.get_index(Rol.ADMIN)
    user2.person_id = ids[1]
    db.session.add(user2)

    user3 = User("test")
    user3.username = "client@gmail.com"
    user3.set_password("client")
    user3.rol = Rol.get_index(Rol.CLIENT)
    user3.person_id = ids[2]
    db.session.add(user3)

    db.session.commit()

def seed_general():
    seed_persons_users()
    

class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        if (
            input(
                "Are you sure you want to drop all tables and recreate? (y/N)\n"
            ).lower()
            == "y"
        ):
            print("Dropping tables...")
            db.drop_all()
            db.create_all()
            seed_general()
            db.session.commit()
            print("DB successfully seeded.")