from marshmallow import fields, Schema

class CreditSchema(Schema):
    """Credit Schema"""

    id = fields.Number(attribute="id")
    amount = fields.Number(attribute="amount")
    request_credit_id = fields.Number(attribute="credit_request_id")
    answer_date = fields.DateTime(attribute="answer_date")
    state = fields.Number(attribute="state")
    user_id = fields.Number(attribute="user_id")
    description = fields.String(attribute="description")


class RequestCreditSchema(Schema):
    """Request Credit Schema"""

    id = fields.Number(attribute="id")
    amount = fields.Number(attribute="amount")
    state = fields.Number(attribute="state")
    user_id = fields.Number(attribute="user_id")
