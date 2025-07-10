from Builder.concrete_builders import GamingComputerBuilder, OfficeComputerBuilder
from Builder.director import ComputerDirector


def build_and_show_computer(builder_type: str):
    """构建并展示计算机配置的辅助函数"""

    # 根据类型选择建造者
    if builder_type.lower() == "gaming":
        print("\nBuilding a Gaming Computer:")
        builder = GamingComputerBuilder()
    elif builder_type.lower() == "office":
        print("\nBuilding an Office Computer:")
        builder = OfficeComputerBuilder()
    else:
        raise ValueError("Unknown computer type")

    # 创建指挥者并构建计算机
    director = ComputerDirector(builder)
    director.construct_computer()

    # 获取并展示构建的计算机
    computer = director.get_computer()
    computer.show_specs()


if __name__ == "__main__":
    # 构建并展示游戏电脑
    build_and_show_computer("gaming")

    # 构建并展示办公电脑
    build_and_show_computer("office")