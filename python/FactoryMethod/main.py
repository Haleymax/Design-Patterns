from FactoryMethod.implement import SeaLogistics, RoadLogistics
from FactoryMethod.interface import Logistics


def client_code(logistics: Logistics) -> None:
    """
    客户端代码与具体创建者类的实例一起工作，尽管通过其基本接口。
    只要客户端继续通过基本接口与创建者合作，你就可以将任何创建者的子类传递给它。
    """
    print(f"Client: I'm not aware of the logistics class, but it still works.\n"
          f"{logistics.plan_delivery()}", end="")


if __name__ == "__main__":
    print("App: Launched with RoadLogistics.")
    client_code(RoadLogistics())
    print("\n")

    print("App: Launched with SeaLogistics.")
    client_code(SeaLogistics())