"""
复合节点实现 - 文件夹类
表示文件系统中的文件夹，可以包含其他文件或文件夹
"""
from typing import List

from .file_system_component import FileSystemComponent

class Directory(FileSystemComponent):
    """复合节点类，表示文件夹，可以包含其他文件或文件夹"""

    def __init__(self, name: str):
        """
        初始化文件夹对象

        Args:
            name: 文件夹名称
        """
        self.name = name
        self.children: List[FileSystemComponent] = []

    def display(self, indent: int = 0) -> None:
        """显示文件夹及其所有内容"""
        print('  ' * indent + f"📁 {self.name}/ (总大小: {self.get_size()} bytes)")
        # 递归显示所有子组件
        for child in self.children:
            child.display(indent + 1)

    def get_size(self) -> int:
        """计算文件夹内所有内容的总大小"""
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

    def add(self, component: FileSystemComponent) -> None:
        """添加子组件到文件夹"""
        self.children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        """从文件夹中移除子组件"""
        self.children.remove(component)

    def get_children(self) -> List[FileSystemComponent]:
        """获取文件夹中的所有子组件"""
        return self.children

    def __str__(self) -> str:
        return  f"Directory(name={self.name}, children_count={len(self.children)})"

    def __repr__(self) -> str:
        return self.__str__()