from flask import Flask
from flask_orator import Orator
from config import config
from flask_bootstrap import Bootstrap

db = Orator()
bootstrap = Bootstrap()


def create_app(config_name='develop'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.jinja_env.auto_reload = True
    db.init_app(app)
    bootstrap.init_app(app)

    from .mian_views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .filter import register_template_filter
    register_template_filter(app)
    return app
