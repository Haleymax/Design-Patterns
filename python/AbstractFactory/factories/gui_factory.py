"""
GUI工厂抽象模块 - 定义创建GUI组件的抽象工厂接口
"""
from abc import ABC, abstractmethod

from AbstractFactory.gui_elements.buttons import Button
from AbstractFactory.gui_elements.checkboxes import CheckBox


class GuiFactory(ABC):
    """
    抽象工厂接口，声明创建一系列相关产品的方法
    每个具体工厂都会实现这些方法来创建特定风格的产品
    """

    @abstractmethod
    def create_button(self) -> Button:
        """创建按钮产品的抽象方法"""
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        """创建复选框产品的抽象方法"""
        pass