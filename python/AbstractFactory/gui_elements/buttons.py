"""
按钮模块 - 包含按钮的抽象类和具体实现
定义了GUI按钮的通用接口和不同平台的具体实现
"""

from abc import ABC, abstractmethod

class Button(ABC):
    """按钮抽象基类，定义所有按钮必须实现的方法"""

    @abstractmethod
    def render(self):
        """渲染按钮到屏幕的抽象方法"""
        pass

    @abstractmethod
    def on_click(self):
        """处理点击事件的抽象方法"""
        pass

class MacButton(Button):
    """Mac风格按钮的具体实现"""

    def render(self):
        """实现Mac风格按钮的渲染逻辑"""
        print("渲染一个Mac风格的按钮")

    def on_click(self):
        """实现Mac风格按钮的点击事件处理"""
        print("Mac按钮被点击")


class WindowsButton(Button):
    """Windows风格"""

    def render(self):
        """实现Windows风格按钮的渲染逻辑"""
        print("渲染一个Windows风格的按钮")

    def on_click(self):
        """实现Windows风格按钮的点击事件处理"""
        print("Windows按钮被点击")