from flask import Blueprint, request
from models.sales import Sales, SalesSchema
from models.clients import Clients
from models.products import Products
import datetime


reportsRoutes = Blueprint("reports", __name__)

salesSchema = SalesSchema(many=True)


@reportsRoutes.route("/reports", methods=["POST"])
def getReport():
    try:
        product_id = request.json.get('product_id')
        client_document = request.json.get("client_document")
        sale_date = request.json.get("sale_date")

        sales = Sales.query.join(Products, Sales.product_id == Products.id).join(
            Clients, Sales.client_id == Clients.id
        )

        if product_id:
            sales = sales.filter(Products.id == product_id)

        if client_document:
            sales = sales.filter(Clients.client_document == client_document)

        if sale_date:
            sales = sales.filter(Sales.sale_date == sale_date)

        sales = sales.all()
        return salesSchema.jsonify(sales)
    except Exception as e:
        return {"error": e}, 500
