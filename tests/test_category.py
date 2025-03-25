import pytest
from src.product import Smartphone, LawnGrass
from src.category import Category

def test_product_addition():
    smartphone = Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, "High", "15", "512GB", "Gray")
    grass = LawnGrass("Классическая", "Газонная трава", 500.0, 20, "Россия", "7 дней", "Зеленый")
    category = Category("Разное", "Разные товары")
    category.add_product(smartphone)
    category.add_product(grass)
    assert category.product_count == 2

def test_product_addition_invalid():
    category = Category("Разное", "Разные товары")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")