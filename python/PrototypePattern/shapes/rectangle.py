from PrototypePattern.shapes.shape import Shape


class Rectangle(Shape):
    """
    具体原型类 - 矩形
    实现矩形特有的属性和方法
    """

    def __init__(self):
        super().__init__()
        self.type = 'Rectangle'
        # 可以添加矩形特有属性，如长宽
        self.width = 0
        self.height = 0

    def draw(self):
        """实现矩形的绘制方法"""
        print(f"Drawing Rectangle(id={self.id}), width={self.width}, height={self.height})")

    def set_dimensions(self, width, height):
        """设置矩形尺寸"""
        self.width = width
        self.height = height