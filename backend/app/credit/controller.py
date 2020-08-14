from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import CreditSchema, RequestCreditSchema
from .service import CreditService, RequestCreditService
from .model import Credit, RequestCredit
from .interface import CreditInterface, RequestCreditInterface

credit_api = Namespace("Credit", description="Credit")

@credit_api.route("/", strict_slashes=False)
class CreditResource(Resource):
    """Credits"""

    @responds(schema=CreditSchema(many=True))
    def get(self) -> List[Credit]:
        """Get all Credits"""

        return CreditService.get_all()

    @accepts(schema=CreditSchema, api=credit_api)
    @responds(schema=CreditSchema)
    def post(self) -> Credit:
        """Create a Single Credit"""

        return CreditService.create(request.parsed_obj)


@credit_api.route("/<int:id>")
@credit_api.param("id", "Credit database ID")
class CreditIdResource(Resource):
    @responds(schema=CreditSchema)
    def get(self, id: int) -> Credit:
        """Get Single Credit"""

        return CreditService.get_by_id(id)

    def delete(self, id: int) -> Response:
        """Delete Single Credit"""
        from flask import jsonify

        id = CreditService.delete_by_id(id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=CreditSchema, api=credit_api)
    @responds(schema=CreditSchema)
    def put(self, id: int) -> Credit:
        """Update Single Credit"""

        changes: CreditInterface = request.parsed_obj
        credit = CreditService.get_by_id(id)
        return CreditService.update(credit, changes)


request_credit_api = Namespace("RequestCredit", description="RequestCredit")

@request_credit_api.route("/", strict_slashes=False)
class RequestCreditResource(Resource):
    """RequestCredits"""

    @responds(schema=RequestCreditSchema(many=True))
    def get(self) -> List[RequestCredit]:
        """Get all RequestCredits"""

        return RequestCreditService.get_all()

    @accepts(schema=RequestCreditSchema, api=request_credit_api)
    @responds(schema=RequestCreditSchema)
    def post(self) -> RequestCredit:
        """Create a Single RequestCredit"""

        return RequestCreditService.create(request.parsed_obj)


@request_credit_api.route("/<int:id>")
@request_credit_api.param("id", "RequestCredit database ID")
class RequestCreditIdResource(Resource):
    @responds(schema=RequestCreditSchema)
    def get(self, id: int) -> RequestCredit:
        """Get Single RequestCredit"""

        return RequestCreditService.get_by_id(id)

    def delete(self, id: int) -> Response:
        """Delete Single RequestCredit"""
        from flask import jsonify

        id = RequestCreditService.delete_by_id(id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=RequestCreditSchema, api=request_credit_api)
    @responds(schema=RequestCreditSchema)
    def put(self, id: int) -> RequestCredit:
        """Update Single RequestCredit"""

        changes: RequestCreditInterface = request.parsed_obj
        request_credit = RequestCreditService.get_by_id(id)
        return RequestCreditService.update(request_credit, changes)