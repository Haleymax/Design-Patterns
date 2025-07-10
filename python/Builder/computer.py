from typing import Any


class Computer:
    """产品类 - 表示最终要构建的复杂对象（计算机）"""

    def __init__(self):
        # 使用字典存储计算机的各个组件及其规格
        self._components = {}

    def add_component(self, component: str, specification: Any) -> None:
        """ 添加计算机组件及其规格

        :param component: 组件名词 （如CPU、RAM等）
        :param specification: 组件规格
        """
        self._components[component] = specification

    def show_specs(self) -> None:
        """展示计算机的所有配置信息"""
        print("Computer Specifications:")
        for component, spec in self._components.items():
            print(f"{component}: {spec}")
        print()

    def get_components(self) -> dict:
        """获取所有组件配置"""
        return self._components