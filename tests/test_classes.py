import pytest
from src.class_init import Product, Category


@pytest.fixture
def sample_product():
    return Product("Smartphone", "Latest model", 699.99, 50)


@pytest.fixture
def sample_category():
    return Category("Electronics", "Various electronic devices")


def test_product_initialization(sample_product):
    assert sample_product.name == "Smartphone"
    assert sample_product.description == "Latest model"
    assert sample_product.price == 699.99
    assert sample_product.quantity == 50


def test_category_initialization(sample_category):
    assert sample_category.name == "Electronics"
    assert sample_category.description == "Various electronic devices"
    assert len(sample_category.products) == 0


def test_category_count():
    initial_count = Category.category_count
    Category("Appliances", "Home appliances")
    assert Category.category_count == initial_count + 1


def test_product_count_in_category(sample_category, sample_product):
    initial_product_count = Category.product_count
    sample_category.add_product(sample_product)
    assert len(sample_category.products) == 1
    assert Category.product_count == initial_product_count + 1
