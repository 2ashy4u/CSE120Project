from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

#initializes Database
db = SQLAlchemy()
DB_NAME= "database.db"


#initializes Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'westernDigital'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)



    from .views import views
    from .auth import auth
    #register blueprints for flask
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    create_database(app)
    
    return app

#inititalizes database
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
