from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getcwd

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random_string'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import view_blueprint
    
    app.register_blueprint(view_blueprint, url_prefix='/')
    
    with app.app_context():
        create_database(app) 
        
    return app

def create_database(app):
    print("Current working directory:", getcwd())  
    if not path.exists(path.join(getcwd(), 'application', DB_NAME)):
        db.create_all() 
        print('Database Created')
