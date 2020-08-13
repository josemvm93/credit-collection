import os
from typing import List, Type

class BaseConfig:
    CONFIG_NAME = "base"
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_DEV_URI')

class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    DEBUG = False
    TESTING = False

EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}