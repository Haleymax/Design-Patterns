from FactoryMethod.interface import Transport, Logistics


# 具体产品 - 卡车
class Truck(Transport):
    def deliver(self) -> str:
        return "Delivering by land in a box"

# 具体产品 - 轮船
class Ship(Transport):
    def deliver(self) -> str:
        return "Delivering by sea in a container"


# 具体创建者 - 公路物流
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

# 具体创建者 - 海运物流
class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

