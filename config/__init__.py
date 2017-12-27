from .db import DATABASES


class Config:
    SECRET_KEY = ''
    DEBUG = False

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    DEBUG = True
    ORATOR_DATABASES = DATABASES


class ProductConfig(Config):
    ORATOR_DATABASES = DATABASES


config = {
    'develop': DevelopConfig,
    'product': ProductConfig
}
