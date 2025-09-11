"""
客户端代码：使用外观类来简化与子系统的交互
"""
from facade.facede import ComputerFacade, AdvancedComputerFacade


def demo_basic_facade():
    """演示基本外观模式的使用"""
    print("基本外观模式演示:")
    print("-" * 30)

    # 创建外观对象
    computer = ComputerFacade()

    # 使用简化的接口启动计算机
    computer.start()

    print("\n")


def demo_advanced_facade():
    """演示高级外观模式的使用"""
    print("高级外观模式演示:")
    print("-" * 30)

    # 创建高级外观对象
    advanced_computer = AdvancedComputerFacade()

    # 使用简化的接口操作计算机
    advanced_computer.start()
    print()  # 空行

    # 重启计算机
    advanced_computer.restart()
    print()  # 空行

    # 关闭计算机
    advanced_computer.shutdown()


def demo_without_facade():
    """演示不使用外观模式的复杂调用"""
    print("不使用外观模式的演示:")
    print("-" * 30)
    print("直接调用子系统组件:")

    # 直接创建和使用子系统组件
    from subsystem import CPU, Memory, HardDrive, BIOS

    cpu = CPU()
    memory = Memory()
    hard_drive = HardDrive()
    bios = BIOS()

    # 需要了解所有子系统的细节和调用顺序
    boot_sector_address = bios.find_boot_sector()
    bios.load_boot_sector(boot_sector_address)
    cpu.freeze()
    boot_program = hard_drive.read(0, 512)
    memory.load(boot_sector_address, boot_program)
    cpu.jump(boot_sector_address)
    cpu.execute()

    print("可以看到，直接调用子系统非常复杂!")
    print("\n")


if __name__ == "__main__":
    # 演示不使用外观模式的复杂性
    demo_without_facade()

    # 演示基本外观模式
    demo_basic_facade()

    # 演示高级外观模式
    demo_advanced_facade()

    print("外观模式的优势:")
    print("1. 简化了客户端与子系统的交互")
    print("2. 将客户端与子系统解耦")
    print("3. 如果需要，仍然可以直接访问子系统")
    print("4. 符合'最少知识原则'")