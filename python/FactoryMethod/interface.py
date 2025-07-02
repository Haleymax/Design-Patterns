from abc import ABC, abstractmethod

# 产品接口
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


# 创建者接口
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self) -> str:
        # 调用工厂方法创建一个运输对象
        transport = self.create_transport()
        # 使用产品
        result = f"Logistics: {transport.deliver()}"
        return result