"""
调料模块：定义调料装饰器
"""
from abc import ABC, abstractmethod

from Decorator.beverages import Beverage


class CondimentDecorator(Beverage, ABC):
    """
    调料装饰器抽象类：继承自Beverage，确保接口一致
    """
    def __init__(self, beverage: Beverage) -> None:
        super().__init__()
        self.beverage = beverage

    @abstractmethod
    def get_description(self) -> str:
        pass

class Mocha(CondimentDecorator):
    """
    摩卡调料 - 具体装饰器
    """
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20

class Soy(CondimentDecorator):
    """
    豆浆调料 - 具体装饰器
    """
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return self.beverage.cost() + 0.15

class Whip(CondimentDecorator):
    """
    奶泡调料 - 具体装饰器
    """
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10

class SteamedMild(CondimentDecorator):
    """
    蒸奶调料 - 具体装饰器
    """
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Steamed Mild"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10

class Caramel(CondimentDecorator):
    """
    焦糖调料 - 具体装饰器
    """
    def get_description(self) -> str:
        return self.beverage.get_description() + ", Caramel"

    def cost(self) -> float:
        return self.beverage.cost() + 0.25
