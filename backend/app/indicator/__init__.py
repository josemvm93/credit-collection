from .model import Indicator
from .schema import IndicatorSchema

BASE_ROUTE_INDICATOR = "indicator"

def register_routes(api, app, root="api"):
    from .controller import indicator_api

    api.add_namespace(indicator_api, path=f"/{root}/{BASE_ROUTE_INDICATOR}")