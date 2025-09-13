"""
叶子节点实现 - 文件类
表示文件系统中的文件
"""
from .file_system_component import FileSystemComponent

class File(FileSystemComponent):
    """叶子节点类，表示文件"""

    def __init__(self, name:str, size:int):
        """
        初始化文件对象

        Args:
             name: 文件名
             size: 文件大小（字节）
        """
        self.name = name
        self.size = size

    def display(self, indent:int = 0) -> None:
        """显示文件信息"""
        # 使用缩进表示层次结构
        print('  ' * indent + f"📄 {self.name} ({self.size} bytes)")

    def get_size(self) -> int:
        """获取文件大小"""
        return self.size

    def __str__(self) -> str:
        return f"File(name={self.name}, size={self.size})"