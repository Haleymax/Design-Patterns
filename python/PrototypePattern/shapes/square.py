from PrototypePattern.shapes.shape import Shape


class Square(Shape):
    """
    具体原型类 - 正方形
    实现正方形特有的属性和方法
    """

    def __init__(self):
        super().__init__()
        self.type = "Square"
        # 可以添加正方形特有属性，如边长
        self.side_length = 0

    def draw(self):
        """实现正方形的绘制方案"""
        print(f"Drawing Square(id={self.id}, side={self.side_length})")

    def set_side(self, length):
        """设置正方形边长"""
        self.side_length = length