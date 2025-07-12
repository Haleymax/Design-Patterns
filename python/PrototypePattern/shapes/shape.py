import copy
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    抽象原型基类
    定义克隆接口和基本形状属性
    使用抽象基类确保子类实现必要方法
    """

    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def draw(self):
        """抽象方法，子类必须实现绘制逻辑"""
        pass

    def clone(self):
        """
        克隆方法
        使用深拷贝创建对象副本
        返回：新克隆的形状对象
        """
        return copy.deepcopy(self)


    def get_id(self):
        """获取形状id"""
        return self.id

    def set_id(self, shape_id):
        """设置形状id"""
        self.id = shape_id

    def get_type(self):
        """获取形状类型"""
        return self.type

    def __str__(self):
        """字符串表示，便于调试"""
        return f"{self.type}(id={self.get_id()})"