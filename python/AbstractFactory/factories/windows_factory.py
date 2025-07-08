"""
Windows风格工厂模块 - 实现创建Windows风格GUI组件的具体工厂
"""

from AbstractFactory.factories.gui_factory import GuiFactory
from AbstractFactory.gui_elements.buttons import WindowsButton
from AbstractFactory.gui_elements.checkboxes import WindowsCheckbox


class WindowsFactory(GuiFactory):
    """
    Windows风格的具体工厂，实现创建Windows风格产品的方法
    每个方法返回一个具体的Windows风格产品
    """

    def create_button(self):
        """创建Windows风格按钮"""
        return WindowsButton()

    def create_checkbox(self):
        """创建Windows风格复选框"""
        return WindowsCheckbox()