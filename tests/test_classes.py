import unittest
import logging
from src.class_init import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    def test_price_getter(self):
        self.assertEqual(self.product.price, 180000.0)

    def test_price_setter_valid(self):
        self.product.price = 190000.0
        self.assertEqual(self.product.price, 190000.0)

    def test_price_setter_negative(self):
        with self.assertLogs(level='WARNING') as cm:
            self.product.price = -100
        self.assertIn("Цена не должна быть нулевая или отрицательная", cm.output[0])
        self.assertEqual(self.product.price, 180000.0)

    def test_price_setter_zero(self):
        with self.assertLogs(level='WARNING') as cm:
            self.product.price = 0
        self.assertIn("Цена не должна быть нулевая или отрицательная", cm.output[0])
        self.assertEqual(self.product.price, 180000.0)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
