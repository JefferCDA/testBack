from flask import Blueprint, request
from models.sales import Sales, SalesSchema
from models.clients import Clients
from models.products import Products

reportsRoutes = Blueprint("reports", __name__)

salesSchema = SalesSchema(many=True)


@reportsRoutes.route("/reports")
def getReport():
    try:
        product_id = request.args.get("product_id")
        client_document = request.args.get("client_document")
        sales_date = request.args.get("sales_date")

        sales = Sales.query.join(Products, Sales.product_id == Products.id).join(
            Clients, Sales.client_id == Clients.id
        )

        if product_id:
            sales = sales.filter(Products.product_code == product_id)

        if client_document:
            sales = sales.filter(Clients.client_document == client_document)

        if sales_date:
            sales = sales.filter(Sales.sales_date == sales_date)

        sales = sales.all()
        return salesSchema.jsonify(sales)
    except Exception as e:
        return {"error": e}, 500
