from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import mysql.connector

# initializes Database
db = SQLAlchemy()
DB_NAME = "userdb"
# initializes Flask

conn = mysql.connector.connect(
    user='root',
    password='12345678',
    host='127.0.0.1',
    database='userdb'
)

cursor = conn.cursor()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'westernDigital'

    # below requires existing database called 'userdb' / Connects to local Database
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f'mysql://root:12345678@127.0.0.1:3306/{DB_NAME}'
# initializes database with app
    db.init_app(app)
# more improrts from different files
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
