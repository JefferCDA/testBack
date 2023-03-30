from utils.configdb import db, ma
from datetime import datetime

class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product_quantity = db.Column(db.Integer, default = 1)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    total = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, default=0)
    sale_date = db.Column(db.Date, default=datetime.utcnow)

    def __init__(self, product_id,product_quantity, client_id,total,discount,sale_date):
        self.product_id = product_id
        self.product_quantity = product_quantity
        self.client_id = client_id
        self.total = total
        self.discount = discount
        self.sale_date = sale_date

class SalesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'product_id','product_quantity', 'client_id','total', 'discount','sale_date')
