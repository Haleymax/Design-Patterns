from Builder.builder import ComputerBuilder
from Builder.computer import Computer


class ComputerDirector:
    """指挥者类 - 负责控制构建过程"""

    def __init__(self, builder: ComputerBuilder):
        # 接收一个具体的建造者对象
        self._builder = builder

    def construct_computer(self) -> None:
        """按照特定顺序调用建造者的方法来构建产品"""
        self._builder.build_cpu()  # 第一步：构建CPU
        self._builder.build_ram()  # 第二步：构建内存
        self._builder.build_storage()  # 第三步：构建存储
        self._builder.build_gpu()  # 第四步：构建显卡
        self._builder.build_monitor()  # 第五步：构建显示器

    def get_computer(self) -> Computer:
        """返回构建完成的产品"""
        return self._builder.computer

    def change_builder(self, builder: ComputerBuilder) -> None:
        """更换建造者"""
        self._builder = builder