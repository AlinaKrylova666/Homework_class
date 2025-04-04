import unittest
from src.class_init import Product, Category

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    def test_price_getter(self):
        self.assertEqual(self.product1.price, 180000.0)

    def test_price_setter_valid(self):
        self.product1.price = 190000.0
        self.assertEqual(self.product1.price, 190000.0)

    def test_price_setter_negative(self):
        with self.assertLogs(level='WARNING') as cm:
            self.product1.price = -100
        self.assertIn("Цена не должна быть нулевая или отрицательная", cm.output[0])
        self.assertEqual(self.product1.price, 180000.0)

    def test_price_setter_zero(self):
        with self.assertLogs(level='WARNING') as cm:
            self.product1.price = 0
        self.assertIn("Цена не должна быть нулевая или отрицательная", cm.output[0])
        self.assertEqual(self.product1.price, 180000.0)

    def test_product_str_representation(self):
        expected_str = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        self.assertEqual(str(self.product1), expected_str)

    def test_product_addition(self):
        # Проверка сложения двух продуктов
        total_value = self.product1 + self.product2
        expected_value = (180000.0 * 5) + (210000.0 * 8)
        self.assertEqual(total_value, expected_value)

class TestCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        self.category = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [self.product1, self.product2, self.product3]
        )

    def test_category_str_representation(self):
        expected_str = "Смартфоны, количество продуктов: 27 шт."
        self.assertEqual(str(self.category), expected_str)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()
