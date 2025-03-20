import logging

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут с двойным подчеркиванием
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            logging.warning("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_info):
        return cls(
            product_info['name'],
            product_info['description'],
            product_info['price'],
            product_info['quantity']
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented

class Category:
    category_count = 0
    _total_product_count = 0  # Изменение имени атрибута класса

    def __init__(self, name: str, description: str, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут для хранения списка товаров

        # Увеличиваем количество категорий при создании нового объекта
        Category.category_count += 1

        # Увеличиваем количество товаров при добавлении продуктов в новую категорию
        Category._total_product_count += len(products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category._total_product_count += 1
        else:
            raise TypeError("Ожидается объект класса Product")

    @property
    def products(self):
        # Оптимизация: использование строкового представления продукта
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_count(self):
        return len(self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

# Пример использования
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
