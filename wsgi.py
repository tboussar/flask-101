# wsgi.py
from flask import Flask, jsonify
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
    pos = int(id) - 1
    try:
        product = the_products[pos]
        return jsonify(product), 200
    except:
        return 'notfound', 404
