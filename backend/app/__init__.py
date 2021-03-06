from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_seeder import FlaskSeeder
from flask_cors import CORS

def create_app(env=None):
    from .db import db
    from .ext import ma, migrate
    from .config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "dev"])

    api = Api(app, title="Credit Collection API", version="0.1.0")

    register_routes(api, app)

    db.init_app(app)

    ma.init_app(app)
    migrate.init_app(app, db)


    seeder = FlaskSeeder()
    seeder.init_app(app, db)
    CORS(app)

    return app