"""
客户端代码：演示咖啡店订单系统的装饰器模式
"""
from random import betavariate

from Decorator.beverages import Beverage, Espresso, HouseBlend, DarkRoast, Decaf
from Decorator.condiments import Mocha, Whip, Soy, SteamedMild, Caramel


def print_order(beverage):
    """打印订单详情"""
    print(f"{beverage.get_description()} ${beverage.cost():.2f}")

def main():
    """
    主函数：演示各种咖啡订单
    """
    print("=== 欢迎来到星巴克咖啡店 ===")
    print("\n1. 基础咖啡：")

    # 基础咖啡
    espresso = Espresso()
    print(espresso)

    house_blend = HouseBlend()
    print_order(house_blend)

    dark_roast = DarkRoast()
    print_order(dark_roast)

    decaf = Decaf()
    print_order(decaf)

    print("\n2. 加调料的咖啡:")

    # 浓缩咖啡 + 双倍摩卡 + 奶泡
    beverage1 = Espresso()
    beverage1 = Mocha(beverage1) # 第一次加摩卡
    beverage1 = Mocha(beverage1) # 第二次加摩卡
    beverage1 = Whip(beverage1)  # 加奶泡
    print_order(beverage1)

    # 深度烘培咖啡 + 摩卡 + 奶泡
    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print_order(beverage2)

    # 家常咖啡 + 豆浆 + 摩卡 + 奶泡
    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print_order(beverage3)

    # 脱因咖啡 + 蒸奶 + 焦糖 + 双倍奶泡
    beverage4 = Decaf()
    beverage4 = SteamedMild(beverage4)
    beverage4 = Caramel(beverage4)
    beverage4 = Whip(beverage4)
    beverage4 = Whip(beverage4) # 双倍奶泡
    print_order(beverage4)

    print("\n3. 复杂订单示例:")

    # 创建一个豪华订单
    print("豪华套餐:")
    premium_coffee = DarkRoast()
    premium_coffee = Mocha(premium_coffee)
    premium_coffee = Caramel(premium_coffee)
    premium_coffee = SteamedMild(premium_coffee)
    premium_coffee = Whip(premium_coffee)
    print_order(premium_coffee)

    # 创建一个健康订单
    print("\n健康选择:")
    healthy_coffee = HouseBlend()
    healthy_coffee = Soy(healthy_coffee)
    healthy_coffee = SteamedMild(healthy_coffee)
    print_order(healthy_coffee)

def interactive_order():
    """
    交互式点单系统
    """
    print("\n=== 交互式点单系统 ===")

    # 选择基础咖啡
    print("\n请选择基础咖啡:")
    print("1. 浓缩咖啡 (Espresso) - $1.99")
    print("2. 家常咖啡 (House Blend) - $0.89")
    print("3. 深度烘焙 (Dark Roast) - $0.99")
    print("4. 脱因咖啡 (Decaf) - $1.05")

    choice = input("请输入选择 (1-4): ")
    if choice == "1":
        beverage = Espresso()
    elif choice == "2":
        beverage = HouseBlend()
    elif choice == "3":
        beverage = DarkRoast()
    elif choice == "4":
        beverage = Decaf()
    else:
        print("无效选择，默认选择家常咖啡")
        beverage = HouseBlend()

    # 选择调料
    print("\n请选择调料 (可多选，输入0结束):")
    print("1. 摩卡 (+$0.20)")
    print("2. 豆浆 (+$0.15)")
    print("3. 奶泡 (+$0.10)")
    print("4. 蒸奶 (+$0.10)")
    print("5. 焦糖 (+$0.25)")
    print("0. 完成点单")

    while True:
        condiment_choice = input("请输入调料选择 (0-5): ")

        if condiment_choice == "0":
            break
        elif condiment_choice == "1":
            beverage = Mocha(beverage)
            print("已添加摩卡")
        elif condiment_choice == "2":
            beverage = Soy(beverage)
            print("已添加豆浆")
        elif condiment_choice == "3":
            beverage = Whip(beverage)
            print("已添加奶泡")
        elif condiment_choice == "4":
            beverage = SteamedMild(beverage)
            print("已添加蒸奶")
        elif condiment_choice == "5":
            beverage = Caramel(beverage)
            print("已添加焦糖")
        else:
            print("无效选择")

        # 显示最终订单
    print("\n=== 您的订单 ===")
    print_order(beverage)

if __name__ == "__main__":
    # 运行演示示例
    main()

    # 运行交互式点单系统
    interactive_order()