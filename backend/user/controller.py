from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import UserSchema, PersonSchema
from .service import UserService, PersonService
from .model import User, Person
from .interface import UserInterface, PersonInterface

user_api = Namespace("User", description="User")

@user_api.route("/")
class UserResource(Resource):
    """Users"""

    @responds(schema=UserSchema(many=True))
    def get(self) -> List[User]:
        """Get all Users"""

        return UserService.get_all()

    @accepts(schema=UserSchema, api=user_api)
    @responds(schema=UserSchema)
    def post(self) -> User:
        """Create a Single User"""

        return UserService.create(request.parsed_obj)


@user_api.route("/<int:id>")
@user_api.param("id", "User database ID")
class UserIdResource(Resource):
    @responds(schema=UserSchema)
    def get(self, id: int) -> User:
        """Get Single User"""

        return UserService.get_by_id(id)

    def delete(self, id: int) -> Response:
        """Delete Single User"""
        from flask import jsonify

        id = UserService.delete_by_id(id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=UserSchema, api=user_api)
    @responds(schema=UserSchema)
    def put(self, id: int) -> User:
        """Update Single User"""

        changes: UserInterface = request.parsed_obj
        user = UserService.get_by_id(id)
        return UserService.update(user, changes)


person_api = Namespace("Person", description="Person")

@person_api.route("/")
class PersonResource(Resource):
    """Persons"""

    @responds(schema=PersonSchema(many=True))
    def get(self) -> List[Person]:
        """Get all Persons"""

        return PersonService.get_all()

    @accepts(schema=PersonSchema, api=person_api)
    @responds(schema=PersonSchema)
    def post(self) -> Person:
        """Create a Single Person"""

        return PersonService.create(request.parsed_obj)


@person_api.route("/<int:id>")
@person_api.param("id", "Person database ID")
class PersonIdResource(Resource):
    @responds(schema=PersonSchema)
    def get(self, id: int) -> Person:
        """Get Single Person"""

        return PersonService.get_by_id(id)

    def delete(self, id: int) -> Response:
        """Delete Single Person"""
        from flask import jsonify

        id = PersonService.delete_by_id(id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=PersonSchema, api=person_api)
    @responds(schema=PersonSchema)
    def put(self, id: int) -> Person:
        """Update Single Person"""

        changes: PersonInterface = request.parsed_obj
        person = PersonService.get_by_id(id)
        return PersonService.update(person, changes)