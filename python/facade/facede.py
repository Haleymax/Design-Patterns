"""
外观类：提供了一个简化的接口来处理复杂的子系统
"""
from facade.subsystem import CPU, Memory, HardDrive, BIOS


class ComputerFacade:
    """计算机外观类，简化计算机启动过程"""

    def __init__(self):
        """初始化所有子系统组件"""
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
        self.bios = BIOS()

    def start(self):
        """启动计算机的简化接口"""
        print("=" * 50)
        print("计算机启动中...")
        print("=" * 50)

        # 1. BIOS查找并加载启动扇区
        boot_sector_address = self.bios.find_boot_sector()
        self.bios.load_boot_sector(boot_sector_address)

        # 2. CPU冻结当前操作
        self.cpu.freeze()

        # 3. 从硬盘读取引导程序
        boot_program = self.hard_drive.read(0, 512)

        # 4. 将引导程序加载到内存
        self.memory.load(boot_sector_address, boot_program)

        # 5. CPU跳转到引导程序并执行
        self.cpu.jump(boot_sector_address)
        self.cpu.execute()

        print("=" * 50)
        print("计算机启动完成!")
        print("=" * 50)

        return True


class AdvancedComputerFacade(ComputerFacade):
    """高级计算机外观类，提供更多功能"""

    def shutdown(self):
        """关闭计算机"""
        print("=" * 50)
        print("计算机关闭中...")
        print("=" * 50)
        print("所有子系统已安全关闭")
        print("=" * 50)
        return True

    def restart(self):
        """重启计算机"""
        print("=" * 50)
        print("计算机重启中...")
        print("=" * 50)
        self.shutdown()
        return self.start()