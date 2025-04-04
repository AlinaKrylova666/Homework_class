import pytest
from src.product1 import Product
from src.base_product import BaseProduct

def test_baseproduct_abstract_methods():
    with pytest.raises(TypeError):
        product = BaseProduct("Продукт1", "Описание продукта", 1200, 10)  # Нельзя создать экземпляр абстрактного класса


def test_product_price_setter():
    product = Product("Продукт1", "Описание продукта", 1200, 10)
    product.price = 1500
    assert product.price == 1500
