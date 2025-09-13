"""
抽象组件接口定义
定义了文件系统组件的通用接口
"""
from abc import ABC, abstractmethod
from typing import List

class FileSystemComponent(ABC):
    """抽象组件类，定义文件系统组件的通用接口"""

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """显示组件信息，indent参数用于控制缩进"""
        pass

    @abstractmethod
    def get_size(self) -> int:
        """获取组件大小（字节）"""
        pass

    def add(self, component: 'FileSystemComponent') -> None:
        """添加子组件，默认实现抛出异常，叶子节点不支持此操作"""
        raise NotImplementedError("叶子节点不支持添加操作")

    def remove(self, component: 'FileSystemComponent') -> None:
        """移除子组件，默认实现抛出异常，叶子节点不支持此操作"""
        raise NotImplementedError("叶子节点不支持移除操作")

    def get_children(self) -> List['FileSystemComponent']:
        return []