from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import IndicatorSchema
from .service import IndicatorService
from .model import Indicator
from .interface import IndicatorInterface

indicator_api = Namespace("Indicator", description="Indicator")

@indicator_api.route("/")
class IndicatorResource(Resource):
    """Indicators"""

    @responds(schema=IndicatorSchema(many=True))
    def get(self) -> List[Indicator]:
        """Get all Indicators"""

        return IndicatorService.get_all()

    @accepts(schema=IndicatorSchema, api=indicator_api)
    @responds(schema=IndicatorSchema)
    def post(self) -> Indicator:
        """Create a Single Indicator"""

        return IndicatorService.create(request.parsed_obj)


@indicator_api.route("/<int:id>")
@indicator_api.param("id", "Indicator database ID")
class IndicatorIdResource(Resource):
    @responds(schema=IndicatorSchema)
    def get(self, id: int) -> Indicator:
        """Get Single Indicator"""

        return IndicatorService.get_by_id(id)

    def delete(self, id: int) -> Response:
        """Delete Single Indicator"""
        from flask import jsonify

        id = IndicatorService.delete_by_id(id)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=IndicatorSchema, api=indicator_api)
    @responds(schema=IndicatorSchema)
    def put(self, id: int) -> Indicator:
        """Update Single Indicator"""

        changes: IndicatorInterface = request.parsed_obj
        indicator = IndicatorService.get_by_id(id)
        return IndicatorService.update(indicator, changes)