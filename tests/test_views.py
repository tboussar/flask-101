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
        self.assertGreater(len(products), 0) # 3 is not a mistake here.

    def test_read_product_200(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertStatus(response, 200)
        self.assertEqual(product['name'], 'Skello')

    def test_read_product_404(self):
        response = self.client.get("/api/v1/products/404")
        self.assertStatus(response, 404)

    def test_delete_product(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        initallen = len(products)
        response = self.client.delete("/api/v1/products/4")
        self.assertStatus(response, 204)
        response = self.client.get("/api/v1/products")
        products = response.json
        newlen = len(products)
        self.assertEqual(newlen, initallen-1)

    def test_create_product(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        initallen = len(products)
        response = self.client.post("/api/v1/products", data={'id': 5, 'name': 'gianluigi'})
        self.assertStatus(response, 201)
        response = self.client.get("/api/v1/products")
        products = response.json
        newlen = len(products)
        self.assertEqual(newlen, initallen+1)

    def test_create_product_ok(self):
        response = self.client.patch("/api/v1/products/2", data={'name': 'zlatan' })
        self.assertStatus(response, 204)
        response = self.client.get("/api/v1/products/2")
        product = response.json
        self.assertEqual(product['name'], 'zlatan')

    def test_create_product_ko(self):
        response = self.client.patch("/api/v1/products/12", data={'name': 'zlatan' })
        self.assertStatus(response, 422)
