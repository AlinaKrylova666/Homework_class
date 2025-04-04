from src.product import Product

class Category:
    category_count = 0
    _total_product_count = 0

    def __init__(self, name: str, description: str, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self.__products = products  # Инициализация приватного атрибута

        Category.category_count += 1
        Category._total_product_count += len(products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category._total_product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

    @property
    def products(self):
        return "\n".join(str(product) for product in self.__products)

    @property
    def product_count(self):
        return len(self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def average_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    def middle_price(self):
        # Создаем метод-обертку, чтобы вызывать average_price
        return self.average_price()
