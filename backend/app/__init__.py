from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

def create_app(env=None):
    from .db import db
    from .ext import ma, migrate
    from .config import config_by_name
    from app.routes import register_routes

    # engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
    # Session = sessionmaker(bind=engine)

    # Base = declarative_base()

    # Base.metadata.create_all(engine)

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "dev"])

    api = Api(app, title="Credit Collection API", version="0.1.0")

    register_routes(api, app)

    db.init_app(app)
    
    ma.init_app(app)
    migrate.init_app(app, db)

    return app