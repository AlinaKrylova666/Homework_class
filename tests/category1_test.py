import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category

def test_category_creation():
    category = Category("Смартфоны", "Описание категории")
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert category.product_count == 0

def test_add_product():
    smartphone = Smartphone("iPhone 15", "512GB, Gray", 210000.0, 8, "High", "15", "512GB", "Gray")
    category = Category("Смартфоны", "Описание категории")
    category.add_product(smartphone)
    assert category.product_count == 1

def test_add_product_invalid():
    category = Category("Разное", "Описание категории")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")  # Попытка добавить не объект Product

def test_average_price():
    smartphone1 = Smartphone("iPhone 15", "512GB, Gray", 210000.0, 8, "High", "15", "512GB", "Gray")
    smartphone2 = Smartphone("Samsung", "256GB, Black", 180000.0, 5, "Medium", "S23", "256GB", "Black")
    category = Category("Смартфоны", "Описание", [smartphone1, smartphone2])
    assert category.average_price() == (210000.0 + 180000.0) / 2

def test_average_price_no_products():
    category = Category("Пусто", "Нет продуктов")
    assert category.average_price() == 0

def test_middle_price():
    smartphone = Smartphone("iPhone 15", "512GB, Gray", 210000.0, 8, "High", "15", "512GB", "Gray")
    category = Category("Смартфоны", "Описание категории", [smartphone])
    assert category.middle_price() == category.average_price()
