from utils.configdb import ma, db

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(255), nullable=False)
    client_document = db.Column(db.String(255), nullable=False, unique=True)
    client_phone = db.Column(db.String(255))
    client_email = db.Column(db.String(255))

    def __init__(self, client_name, client_document, client_phone, client_email):
        self.client_name = client_name
        self.client_document  = client_document
        self.client_phone = client_phone
        self.client_email = client_email

class ClientsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'client_name', 'client_document', 'client_phone', 'client_email')