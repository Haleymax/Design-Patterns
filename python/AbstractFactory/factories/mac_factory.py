"""
Mac风格工厂模块 - 实现创建Mac风格GUI组件的具体工厂
"""
from AbstractFactory.factories.gui_factory import GuiFactory
from AbstractFactory.gui_elements.buttons import MacButton
from AbstractFactory.gui_elements.checkboxes import MacCheckBox


class MacFactory(GuiFactory):
    """
    Mac风格的具体工厂，实现创建Mac风格产品的方法
    每个方法返回一个具体的Mac风格产品
    """

    def create_button(self):
        """创建Mac风格按钮"""
        return MacButton()

    def create_checkbox(self):
        """创建Mac风格复选框"""
        return MacCheckBox()