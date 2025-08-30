"""
代理模块
包含控制对真实对象访问的代理类
"""
from subject import Subject
from real_subject import RealSubject

class Proxy(Subject):
    """
    代理类
    控制对真实对象的访问，可以在调用真实对象前后添加额外逻辑
    实现了与真实对象相同的接口
    """

    def __init__(self, real_subject: RealSubject) -> None: