import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

class Config:
    """Base application configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-fallback-secret-key-12345')
    
    # SQLite database inside the instance directory
    _db_path = (BASE_DIR / 'instance' / 'library.db').as_posix()
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or f'sqlite:///{_db_path}'
    if SQLALCHEMY_DATABASE_URI.startswith('sqlite:///instance/'):
        SQLALCHEMY_DATABASE_URI = f'sqlite:///{_db_path}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Library business default constants
    DEFAULT_LOAN_DAYS = 14
    DEFAULT_DAILY_FINE = 5.0
    DEFAULT_MAX_BOOKS = 3

class DevelopmentConfig(Config):
    """Development environment configuration."""
    DEBUG = True

class TestingConfig(Config):
    """Testing environment configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    """Production environment configuration."""
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
