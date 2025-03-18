import logging

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            logging.warning("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_info):
        return cls(
            product_info['name'],
            product_info['description'],
            product_info['price'],
            product_info['quantity']
        )

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут для хранения списка товаров

        # Увеличиваем количество категорий при создании нового объекта
        Category.category_count += 1

        # Увеличиваем количество товаров при добавлении продуктов в новую категорию
        Category.product_count += len(products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Ожидается объект класса Product")

    @property
    def products(self):
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )

    @property
    def product_count(self):
        return len(self.__products)
