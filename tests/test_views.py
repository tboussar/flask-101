# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 3) # 3 is not a mistake here.

    def test_read_product_200(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertStatus(response, 200)
        self.assertEqual(product['name'], 'Skello')


    def test_read_product_404(self):
        response = self.client.get("/api/v1/products/404")
        self.assertStatus(response, 404)
