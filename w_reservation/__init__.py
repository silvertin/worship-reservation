from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

#import config

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

#db = SQLAlchemy()
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def page_not_found(e):
    return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')
    #app.config.from_object(config)

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    # blueprint
    from .views import main_views, auth_views, menu_views, worship_views, seat_views, worshiptype_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(menu_views.bp)
    app.register_blueprint(worship_views.bp)
    app.register_blueprint(seat_views.bp)
    app.register_blueprint(worshiptype_views.bp)


    # filter
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # Markdown
    #Markdown(app, extensions=['nl2br', 'fenced_code'])

    # 404
    app.register_error_handler(404, page_not_found)

    return app