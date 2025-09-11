"""
子系统类：包含复杂功能的多个类
这些类可以被客户端直接调用，但通常通过外观来简化使用
"""

class CPU:
    """CPU子系统类"""

    def freeze(self):
        """冻结CPU操作"""
        print("CPU: 冻结当前操作")

    def jump(self, position):
        """跳转到指定位置"""
        print(f"CPU: 跳转到内存位置 {position}")

    def execute(self):
        """执行指令"""
        print("CPU: 执行指令")

class Memory:
    """内存子系统类"""

    def load(self, position, data):
        """加载数据到指定内存位置"""
        print(f"内存: 加载数据 '{data}' 到位置 {position}")
        return True

class HardDrive:
    """硬盘子系统类"""

    def read(self, lba, size):
        """从硬盘读取数据"""
        data = f"硬盘数据 (LBA: {lba}, size: {size})"
        print(f"硬盘: 读取数据 '{data}'")
        return data


class BIOS:
    """BIOS子系统类"""

    def find_boot_sector(self):
        """查找启动扇区"""
        print("BIOS: 查找启动扇区")
        return 0x7C00  # 返回启动扇区地址

    def load_boot_sector(self, address):
        """加载启动扇区"""
        print(f"BIOS: 加载启动扇区到内存地址 {address}")
        return True