# -*- coding: utf-8 -*-
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FONDO.db'
db = SQLAlchemy(app)

migrate = Migrate()

# Configuración de la clave secreta para CSRF
app.config['SECRET_KEY'] = 'a9645a7d9d2cb3dea27785d8761674cdc587b0cad0505'

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Importa las rutas después de crear la aplicación para evitar ciclos de importación
from app import routes



def create_app(settings_module):
    # Inicialización de los parámetros de configuración
    ...
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    db.init_app(app)
    migrate.init_app(app, db)
