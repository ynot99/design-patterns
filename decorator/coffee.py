from abc import ABC


class Coffee(ABC):
    def get_cost(self) -> float:
        ...

    def get_description(self) -> str:
        ...
