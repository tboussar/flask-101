# wsgi.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! on est en finale!"


@app.route('/api/v1/products')
def get_products():
    return jsonify(the_products= [
            { 'id': 1, 'name': 'Skello' },
            { 'id': 2, 'name': 'Socialive.tv' }
            ])
