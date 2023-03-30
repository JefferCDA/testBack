from flask import Blueprint, request
from utils.configdb import db
from models.users import Users, UsersSchema
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta

usersRoutes = Blueprint('users', __name__)

userSchema = UsersSchema()
usersSchema = UsersSchema(many= True)

@usersRoutes.route('/users', methods=['POST'])
def setUser():
    try : 
        dataUser = request.get_json()
        
        if  not Users.query.filter_by(user_name = dataUser['user_name']):
            newUser = Users(dataUser['user_name'], dataUser['password'])
            db.session.add(newUser)
            db.session.commit()
            return userSchema.jsonify(newUser)
        else: return  {'error': 'this user already exist'}, 409
    except Exception as e:
        return {'error': e }, 501

@usersRoutes.route('/login', methods=['POST'])
def login():
    try:
        dataUser = request.get_json()
        isUser =Users.query.filter_by(user_name= dataUser['user_name']).first()
        if  isUser:
            if check_password_hash(isUser.password, dataUser['password']):
                return {"access_token": create_access_token(identity=dataUser['user_name'], expires_delta= timedelta(hours=1))}, 200
            else:
                return {"access_token": False}, 403    
        else:  
            return {"access_token": False}, 403
    except Exception as e:
        return {"error": e}, 500 
@usersRoutes.route('/users')
def getUsers():
    allUSers = Users.query.all()
    return usersSchema.jsonify(allUSers)

@usersRoutes.route('/users/<id>', methods=['GET'])
def getUser(id):
    try :
        user = Users.query.get(id)
        if  user != None:
            return userSchema.jsonify(user) 
        else:  return  {'error': 'this user does not exist'}, 404
    except Exception as e: 
        return {'error': e}, 500
