"""
主题接口模块
定义了真实主题和代理都要实现的共同接口
"""
from abc import ABC, abstractmethod

class Subject(ABC):
    """
    主题接口类
    定义了真实对象和代理对象都要实现的方法
    这是代理模式的核心，确保代理和真实对象都有相同的接口
    """

    @abstractmethod
    def request(self) -> None:
        """
        抽象请求方式
        所有具体实现（真实对象和代理）都必须实现这个方法
        """
        pass