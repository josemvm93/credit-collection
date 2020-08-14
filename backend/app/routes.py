def register_routes(api, app, root="api"):
    from .credit import register_routes as attach_credit
    from .user import register_routes as attach_user
    from .indicator import register_routes as attach_indicator
    
    attach_credit(api, app)
    attach_user(api, app)
    attach_indicator(api, app)