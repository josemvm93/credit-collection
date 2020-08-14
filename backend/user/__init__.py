from .model import User, Person
from .schema import UserSchema, PersonSchema

BASE_ROUTE_USER = "user"

BASE_ROUTE_PERSON = "person"


def register_routes(api, app, root="api"):
    from .controller import user_api, person_api

    api.add_namespace(user_api, path=f"/{root}/{BASE_ROUTE_USER}")
    api.add_namespace(person_api, path=f"/{root}/{BASE_ROUTE_PERSON}")