from coffee import Coffee


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def get_cost(self) -> float:
        return self._coffee.get_cost()

    def get_description(self) -> str:
        return self._coffee.get_description()
