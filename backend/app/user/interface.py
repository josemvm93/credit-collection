from mypy_extensions import TypedDict


class UserInterface(TypedDict):
    id: int
    username: str
    password: str
    person_id: int
    rol: int

class PersonInterface(TypedDict):
    id: int
    email: str
    name: str
    last_name: str
    document: str
