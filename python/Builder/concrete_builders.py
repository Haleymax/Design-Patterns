from Builder.builder import ComputerBuilder


class GamingComputerBuilder(ComputerBuilder):
    """游戏电脑建造者 - 构建高性能游戏电脑"""

    def build_cpu(self) -> None:
        # 添加高性能CPU
        self._computer.add_component("CPU", "Intel Core i9-13900K")

    def build_ram(self) -> None:
        # 添加大容量高速内存
        self._computer.add_component("RAM", "32GB DDR5 5600MHz")

    def build_storage(self) -> None:
        # 添加大容量高速固态硬盘
        self._computer.add_component("Storage", "2TB NVMe SSD")

    def build_gpu(self) -> None:
        # 添加高性能独立显卡
        self._computer.add_component("GPU", "NVIDIA RTX 4090")

    def build_monitor(self) -> None:
        # 添加大尺寸高刷新率显示器
        self._computer.add_component("Monitor", "32-inch 4K 144Hz")


class OfficeComputerBuilder(ComputerBuilder):
    """办公电脑建造者 - 构建经济型办公电脑"""

    def build_cpu(self) -> None:
        # 添加中端CPU
        self._computer.add_component("CPU", "Intel Core i5-12400")

    def build_ram(self) -> None:
        # 添加中等容量内存
        self._computer.add_component("RAM", "16GB DDR4 3200MHz")

    def build_storage(self) -> None:
        # 添加中等容量固态硬盘
        self._computer.add_component("Storage", "512GB SSD")

    def build_gpu(self) -> None:
        # 使用集成显卡
        self._computer.add_component("GPU", "Integrated Graphics")

    def build_monitor(self) -> None:
        # 添加普通办公显示器
        self._computer.add_component("Monitor", "24-inch Full HD")
    

