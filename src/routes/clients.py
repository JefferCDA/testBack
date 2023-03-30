from flask import Blueprint, request
from models.clients import Clients, ClientsSchema
from utils.configdb import db

clientsRoutes = Blueprint('clients', __name__)

clientSchema = ClientsSchema()
clientsSchema = ClientsSchema(many=True)


@clientsRoutes.route('/clients', methods=['POST'])
def setClient():
    try: 
        clientData = request.get_json()
        newClient = Clients(clientData['client_name'], clientData['client_document'], clientData['client_phone'], clientData['client_email'])
        
        db.session.add(newClient)
        db.session.commit()

        return clientSchema.jsonify(newClient)
    except Exception as e:
        return {"error": e}, 500


@clientsRoutes.route('/clients')
def getAllClients():
    try:
        allClients = Clients.query.all()
        return clientsSchema.jsonify(allClients)
    except Exception as e:
        return {"error": e}, 500


@clientsRoutes.route('/clients/<id>')
def getClient(id):
    try:
        client = Clients.query.get(id)
        return clientSchema.jsonify(client)
    except Exception as e:
        return {"error": e}, 500
    

@clientsRoutes.route('/clients/<id>', methods = ['PUT'])
def updateClient(id):
    try:
        client = Clients.query.get(id)
        if client is not None:
            client.client_name = request.json.get('client_name', client.client_name)
            client.client_document = request.json.get('client_document', client.client_document)
            client.client_phone = request.json.get('client_phone', client.client_phone)
            client.client_email = request.json.get('client_email', client.client_email)
            db.session.commit()
            return clientSchema.jsonify(client)
        
        else:  return  {'error': 'this user does not exist'}, 404
        
    except Exception as e:
        return {"error": e}, 500