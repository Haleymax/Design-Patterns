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
        """
        初始化代理
        :param real_subject: 要代理的真实对象
        """
        self._real_subject = real_subject
        self._access_count = 0  # 记录访问次数，用于演示额外功能

    def request(self) -> None:
        """
        实现请求方法，在调用真实对象前后可以添加额外逻辑
        如：访问控制、缓存、日志记录、延迟初始化等
        """
        # 调用前的预处理（访问控制、日志等）
        if self.check_access():
            # 调用真实对象的业务逻辑
            self._real_subject.request()
            # 调用后的处理（日志、缓存等）
            self.log_access()


    def check_access(self) -> bool:
        """
        检查访问权限（示例）
        :return: 是否有权限访问
        """
        print("Proxy: 检查访问权限...")
        # 这里可以添加复杂的权限检查逻辑
        # 示例中简单返回True
        return True

    def log_access(self) -> None:
        """
        记录访问日志（示例）
        """
        self._access_count += 1
        print(f"Proxy: 记录访问日志。总访问次数: {self._access_count}")

    def lazy_initialization(self) -> None:
        """
        延迟初始化示例（如果需要）
        只有在真正需要时才创建真实对象
        """
        if self._real_subject is None:
            print("Proxy: 延迟初始化真实对象...")
            self._real_subject = RealSubject()