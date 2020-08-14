from marshmallow import fields, Schema

class UserSchema(Schema):
    """User Schema"""

    id = fields.Number(attribute="id")
    username = fields.String(attribute="username")
    password = fields.String(attribute="password")
    person_id = fields.Number(attribute="person_id")
    rol = fields.Number(attribute="rol")

class PersonSchema(Schema):
    """Person Schema"""

    id = fields.Number(attribute="id")
    name = fields.String(attribute="name")
    last_name = fields.String(attribute="last_name")
    document = fields.Number(attribute="document")
