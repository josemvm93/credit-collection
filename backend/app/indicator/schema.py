from marshmallow import fields, Schema

class IndicatorSchema(Schema):
    """Indicator Schema"""

    id = fields.Number(attribute="id")
    name = fields.String(attribute="username")
    credit_id = fields.Number(attribute="credit_id")
    value = fields.String(attribute="value")