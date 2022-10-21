from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#initializes Database
db = SQLAlchemy()
DB_NAME= "users"

#initializes Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'westernDigital'

    #below requires existing database called 'userdb'
    app.config['SQLALCHEMY_DATABASE_URI']=f'mysql://root:@127.0.0.1:3306/{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth
    #register blueprints for flask
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User
    
    #populate_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #get user id if needed
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

#populate database if not already populated
#def populate_db(app):
        #from .models import User
        #with app.app_context():
            
            #new_user = User(email='YAN.LI@wdc.com',password=generate_password_hash('1234', method='sha256'),firstname='Yan',lastname='Li',employeeID='1',isManager='Y',isSupManager='Y')
                #if not db.session.query(User).filter_by(email='YAN.LI@wdc.com').first():
                    #db.session.add(new_user)
                    #db.session.commit()