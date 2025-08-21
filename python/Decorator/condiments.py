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
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        return self.beverage.cost() + 0.15