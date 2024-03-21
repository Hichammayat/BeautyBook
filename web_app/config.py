class Config:
    """Configuration de base."""
    SECRET_KEY = 'beauty_app'

class DevelopmentConfig(Config):
    """Configuration de développement."""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration de production."""
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)