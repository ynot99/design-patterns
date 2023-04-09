from coffee_decorator import CoffeeDecorator
from coffee import Coffee


class Vanilla(CoffeeDecorator):
    def __init__(self, coffee: Coffee) -> None:
        super().__init__(coffee)

    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.3

    def get_description(self) -> str:
        return self._coffee.get_description() + ", Vanilla"
