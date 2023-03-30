from utils.configdb import db, ma
from werkzeug.security import generate_password_hash

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = generate_password_hash(password)
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_name')