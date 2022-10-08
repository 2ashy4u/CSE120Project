from flask import Flask
#initializes Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'westernDigital'

    from .views import views
    from .auth import auth
    #register blueprints for flask
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app