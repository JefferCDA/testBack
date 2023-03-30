from flask import Blueprint, request
from models.products import Products, ProductSchema
from utils.configdb import db

productsRoutes = Blueprint('products', __name__)

productSchema = ProductSchema()
productsSchema = ProductSchema(many=True)


@productsRoutes.route('/products', methods=['POST'])
def setProduct():
    try: 
        productData = request.get_json()
        newProduct = Products(productData['product_name'], productData['product_price'], productData['product_status'], productData['product_in_stock']) 
        db.session.add(newProduct)
        db.session.commit()

        return productSchema.jsonify(newProduct)    
    
    except Exception as e:
        return {"error": e}, 500

@productsRoutes.route('/products')
def getAllProducts():
    try:
        allProducts = Products.query.all()
        return productsSchema.jsonify(allProducts)
    except Exception as e:
        return {"error": e}, 500
    
@productsRoutes.route('/products/<id>')
def getProduct(id):
    try:
        product = Products.query.get(id)
        return productSchema.jsonify(product)
    except Exception as e:
        return {"error": e}, 500

@productsRoutes.route('/products/<id>', methods = ['PUT'])
def updateClient(id):
    try:
        product = Products.query.get(id)
        if product is not None:
            product.product_name = request.json.get('product_name', product.product_name)
            product.product_price = request.json.get('product_price', product.product_price)
            product.product_status = request.json.get('product_status', product.product_status)
            product.product_in_stock = request.json.get('product_in_stock', product.product_in_stock)
            db.session.commit()
            return productSchema.jsonify(product)
        
        else:  return  {'error': 'this user does not exist'}, 404
        
    except Exception as e:
        return {"error": e}, 500
    
