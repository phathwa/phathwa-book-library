# api/config.py

import os

class Config:
    """Base config class."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'aJNisndsjd6YVHDS') # app key
    API_KEY = os.environ.get("API_KEY", "fake-key")  # Default API key for development

class DevelopmentConfig(Config):
    """Development environment settings."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI', 'sqlite:///library.db')
    DEBUG = True

class AcceptanceConfig(Config): # api docs (/apidocs) more likely to point to
    """Testing environment settings."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI', 'sqlite:///test_library.db')
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """Production environment settings."""
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.environ.get('DATABASE_URI')}"  # treating the EC2 instance as PRD
    DEBUG = False
    TESTING = False