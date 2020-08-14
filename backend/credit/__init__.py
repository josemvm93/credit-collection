from .model import Credit, RequestCredit
from .schema import CreditSchema, RequestCreditSchema

BASE_ROUTE_CREDIT = "credit"

BASE_ROUTE_REQUEST_CREDIT = "request_credit"


def register_routes(api, app, root="api"):
    from .controller import request_credit_api, credit_api

    api.add_namespace(credit_api, path=f"/{root}/{BASE_ROUTE_CREDIT}")
    api.add_namespace(request_credit_api, path=f"/{root}/{BASE_ROUTE_REQUEST_CREDIT}")