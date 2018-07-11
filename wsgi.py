# wsgi.py
from flask import Flask, jsonify, request
app = Flask(__name__)

the_products= [
            { 'id': 1, 'name': 'Skello' },
            { 'id': 2, 'name': 'Socialive.tv' },
            { 'id': 3, 'name': 'Thomas' },
            { 'id': 4, 'name': 'Manu' }
            ]

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/api/v1/products')
def get_products():
    return jsonify(the_products)

@app.route('/api/v1/products/<int:id>', methods=['GET'])
def get_product(id):
    try:
        for product in the_products:
            if product['id'] == id:
                return jsonify(product), 200
        return 'notfound', 404
    except:
        return 'notfound', 404

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def del_product(id):
    pos = int(id) - 1
    try:
        del the_products[pos]
        return 'deleted', 204
    except:
        return 'notfound', 404

@app.route('/api/v1/products', methods=['POST'])
def create_product():
    data=request.form
    the_products.append(data)
    return 'object created', 201

@app.route('/api/v1/products/<int:id>', methods=['PATCH'])
def patch_product(id):
    for product in the_products:
        if product['id'] == id:
            try:
                #product[data[0]] = data[1]
                if request.form.get("name") is not '':
                    product['name'] = request.form.get("name")
                    return 'object edited', 204
            except:
                return 'Error', 422
    return 'Error', 422
