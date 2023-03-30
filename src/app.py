from flask import Flask
from utils.configdb import db
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

from config import Config, DATABASE_CONNECTION_URI, secretKey

# import routes
from routes.clients import clientsRoutes
from routes.products import productsRoutes
from routes.sales import salesRoutes
from routes.users import usersRoutes
from routes.reports import reportsRoutes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 60
app.config['JWT_SECRET_KEY'] = secretKey
app.config['CORS_HEADERS'] = 'Content-Type'

SQLAlchemy(app)
Marshmallow(app)
JWTManager(app)

with app.app_context():
    db.create_all()

app.register_blueprint(clientsRoutes)
app.register_blueprint(productsRoutes)
app.register_blueprint(salesRoutes)
app.register_blueprint(usersRoutes)
app.register_blueprint(reportsRoutes)


if __name__ == '__main__':
    app.config.from_object(Config['development'])
    app.run()