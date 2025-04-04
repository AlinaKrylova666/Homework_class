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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Товары должны быть из одинаковых классов для сложения")

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
