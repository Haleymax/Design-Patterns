"""
客户端模块
演示代理模式的使用
"""
from ProxyPattern.proxy import Proxy
from ProxyPattern.real_subject import RealSubject


def client_code(subject) -> None:
    """
    客户端代码，通过主题接口工作
    不知道它处理的是真实对象还是代理对象
    :param subject: 实现了Subject接口的对象
    """
    print("客户端：开始处理接口工作")
    subject.request()
    print("客户端：请求处理结果!\n")

if __name__ == '__main__':
    print("客户端：直接使用真实对象：")
    real_subject = RealSubject()
    client_code(real_subject)

    print("客户端：通过代理使用真实对象：")
    proxy = Proxy(real_subject)
    client_code(proxy)

    # 演示多次访问以显示代理的额外功能
    print("客户端：多次通过代理访问：")
    for i in range(3):
        print(f"---第 {i+1} 次访问 ---")
        proxy.request()