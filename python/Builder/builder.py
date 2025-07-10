from abc import ABC, abstractmethod

from Builder.computer import Computer


class ComputerBuilder(ABC):
    """抽象建造者 - 定义构建产品的各个步骤的接口"""

    def __init__(self):
        # 初始化时创建一个空的产品对象
        self._computer = Computer()

    @property
    def computer(self) -> Computer:
        """获取构建完成的产品"""
        return self._computer


    # 以下是构建产品的各个抽象方法，需要在具体建造者中实现

    @abstractmethod
    def build_cpu(self) -> None:
        """构建CPU组件"""
        pass

    @abstractmethod
    def build_ram(self) -> None:
        """构建内存组件"""
        pass

    @abstractmethod
    def build_storage(self) -> None:
        """构建存储组件"""
        pass

    @abstractmethod
    def build_gpu(self) -> None:
        """构建显卡组件"""
        pass

    @abstractmethod
    def build_monitor(self) -> None:
        """构建显示器组件"""
        pass