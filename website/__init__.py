from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# initializes Database
db = SQLAlchemy()
DB_NAME = "userdb"

# initializes Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'westernDigital'

    # below requires existing database called 'userdb'
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f'mysql://root:12345678@127.0.0.1:3306/{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth
    # register blueprints for flask#register blueprints for flask
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # get user id
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
