from AbstractFactory.app import Application
from AbstractFactory.factories.mac_factory import MacFactory
from AbstractFactory.factories.windows_factory import WindowsFactory


def client_code():
    """
    客户端代码，演示如何使用抽象工厂模式
    通过切换不同的具体工厂来创建不同风格的产品族
    """
    # 创建Mac风格UI
    print("创建Mac风格UI:")
    mac_factory = MacFactory()  # 创建Mac工厂
    app = Application(mac_factory)  # 应用使用Mac工厂
    app.create_ui()  # 创建Mac风格组件
    app.paint()     # 渲染和交互

    # 创建Windows风格UI
    print("\n创建Windows风格UI:")
    windows_factory = WindowsFactory()  # 创建Windows工厂
    app = Application(windows_factory)  # 应用使用Windows工厂
    app.create_ui()  # 创建Windows风格组件
    app.paint()     # 渲染和交互


if __name__ == "__main__":
    # 程序入口
    client_code()