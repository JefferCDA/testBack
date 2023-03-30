from utils.configdb import db, ma

class Products(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    product_status = db.Column(db.Boolean, nullable=False, default=True)
    product_in_stock = db.Column(db.Integer, nullable=False)

    def __init__ (self ,product_name, product_price, product_status, product_in_stock):
        self.product_name   = product_name
        self.product_price = product_price
        self.product_status = product_status
        self.product_in_stock = product_in_stock

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'product_name', 'product_price', 'product_status', 'product_in_stock')