import pytest
from src.product import Product, Smartphone, LawnGrass

def test_product_creation():
    product = Product("Продукт1", "Описание продукта", 1200, 10)
    assert product.name == "Продукт1"
    assert product.description == "Описание продукта"
    assert product.price == 1200
    assert product.quantity == 10

def test_smartphone_creation():
    smartphone = Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, "High", "15", "512GB", "Gray")
    assert smartphone.name == "iPhone 15"
    assert smartphone.efficiency == "High"

def test_lawngrass_creation():
    grass = LawnGrass("Классическая", "Газонная трава", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass.country == "Россия"

def test_add_same_type():
    smartphone1 = Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, "High", "15", "512GB", "Gray")
    smartphone2 = Smartphone("Samsung", "256GB, Black", 180000.0, 5, "Medium", "S23", "256GB", "Black")
    assert smartphone1 + smartphone2 == 210000.0 * 8 + 180000.0 * 5

def test_add_different_type():
    smartphone = Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, "High", "15", "512GB", "Gray")
    grass = LawnGrass("Классическая", "Газонная трава", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        smartphone + grass

def test_product_str():
    product = Product("Продукт1", "Описание продукта", 1200, 10)
    assert str(product) == "Продукт1, 1200 руб. Остаток: 10 шт."
