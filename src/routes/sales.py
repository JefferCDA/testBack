from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from models.sales import SalesSchema, Sales
from models.products import Products, ProductSchema
from utils.configdb import db
from datetime import datetime


salesRoutes = Blueprint('sales', __name__)

saleSchema = SalesSchema()
salesSchema = SalesSchema(many = True)
productSchema = ProductSchema()

@salesRoutes.route ('/sales', methods = ['POST'])
@jwt_required
def setSale():
    try:
        currentDate = datetime.now()
        if currentDate.day == 15:
            discount = 10
        elif currentDate.day == 30:
            discount = 20
        else: 
            discount = 0

        dataSale = request.get_json()

        productData = Products.query.get(dataSale['product_id'])
        productPrice = productData.product_price

        productQuantity = dataSale['product_quantity']
        if productData.product_in_stock >= productQuantity:

            subtotal = (productQuantity * productPrice)  * (discount / 100)
            total = (productQuantity * productPrice) - subtotal

            newSale = Sales(dataSale['product_id'], productQuantity ,dataSale['client_id'],total, discount, currentDate)
            productData.product_in_stock -= productQuantity

            db.session.add(newSale)
            db.session.commit()

            return saleSchema.jsonify(newSale)
        
        else: return  {'error': 'The quantity of products is not available'}, 404
    except Exception as e:

        return { 'error': e}, 500


@salesRoutes.route ('/sales', methods = ['GET'])
def getAllSales():
    try:
        allSales = Sales.query.all()
        return salesSchema.jsonify(allSales)
    except Exception as e:

        return { 'error': e}, 500

@salesRoutes.route ('/sales/<id>', methods = ['GET'])
def getSale(id):
    try:
        sale = Sales.query.get(id)
        return saleSchema.jsonify(sale)
    except Exception as e:

        return { 'error': e}, 500