class Product:
    def __init__(self, name: str, description: str, price:
float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str,
products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем количество категорий при создании нового объекта
        Category.category_count += 1

        # Увеличиваем количество товаров при добавлении продуктов в новую категорию
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.products.append(product)
        Category.product_count += 1
