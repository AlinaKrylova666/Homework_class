from abc import ABC, abstractmethod

class BaseProduct(ABC):
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass
