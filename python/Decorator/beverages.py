"""
饮料模块：定义饮料抽象类和具体饮料实现
"""
from abc import ABC, abstractmethod

class Beverage(ABC):
    """
    饮料抽象类：定义饮料的接口
    """
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self) -> str:
        """获取饮料描述"""
        return self.description

    @abstractmethod
    def cost(self) -> float:
        """计算饮料价格"""
        pass


class Espresso(Beverage):
    """
    浓缩咖啡 - 具体饮料
    """
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99

class HouseBlend(Beverage):
    """
    家常咖啡 - 具体饮料
    """
    def __init__(self):
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89

class DarkRoast(Beverage):
    """
    深度烘培咖啡 - 具体饮料
    """
    def __init__(self):
        super().__init__()
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    """
    脱因咖啡 - 具体饮料
    """
    def __init__(self):
        super().__init__()
        self.description = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05