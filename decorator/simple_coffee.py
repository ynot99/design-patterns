from coffee import Coffee


class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 2.0

    def get_description(self) -> str:
        return "Simple coffee"
