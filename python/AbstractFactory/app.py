"""
应用模块 - 包含客户端代码，使用抽象工厂创建UI组件
演示如何在不依赖具体类的情况下使用工厂创建产品
"""

from AbstractFactory.factories.gui_factory import GuiFactory


class Application:
    """
    客户端类，通过抽象工厂接口创建和使用产品
    不知道也不关心具体创建的是哪种风格的产品
    """

    def __init__(self, factory: GuiFactory):
        """
        初始化应用，注入一个具体的工厂对象
        :param factory: 实现了GUIFactory接口的具体工厂
        """
        self.factory = factory  # 抽象工厂的引用
        self.button = None  # 按钮产品
        self.checkbox = None  # 复选框产品

    def create_ui(self):
        """使用工厂创建UI组件"""
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        """
        渲染UI并模拟用户交互
        展示了创建的产品可以一起工作，因为它们属于同一产品族
        """
        self.button.render()
        self.checkbox.render()
        self.button.on_click()
        self.checkbox.on_click()