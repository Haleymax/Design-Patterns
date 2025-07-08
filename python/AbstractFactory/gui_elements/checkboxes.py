"""
复选框模块 - 包含复选框的抽象类和具体实现
定义了GUI复选框的通用接口和不同平台的具体实现
"""

from abc import ABC, abstractmethod

class CheckBox(ABC):
    """复选框抽象基类，定义所有复选框必须实现的方法"""

    @abstractmethod
    def render(self):
        """渲染复选框到屏幕的抽象方法"""
        pass

    @abstractmethod
    def on_click(self):
        """处理选中事件的抽象方法"""
        pass


class MacCheckBox(CheckBox):
    """Mac风格复选框的具体实现"""

    def render(self):
        """实现Mac风格复选框的渲染逻辑"""
        print("渲染一个Mac风格的复选框")

    def on_click(self):
        """实现Mac风格复选框中选中事件处理"""
        print("Mac复选框被选中")


class WindowsCheckbox(CheckBox):
    """Windows风格复选框的具体实现"""

    def render(self):
        """实现Windows风格复选框的渲染逻辑"""
        print("渲染一个Windows风格的复选框")

    def on_click(self):
        """实现Windows风格复选框的选中事件处理"""
        print("Windows复选框被选中")

