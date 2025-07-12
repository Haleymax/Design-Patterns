from PrototypePattern.shapes.shape import Shape


class Circle(Shape):
    """
    具体原型类 - 圆型
    实现圆形特有的属性和方法
    """

    def __init__(self):
        super().__init__()
        self.type = 'Circle'
        # 可以添加圆形特有属性，如半径
        self.radius = 0

    def draw(self):
        """实现圆形的绘制方法"""
        print(f"Drawing Circle(id={self.id}, radius={self.radius})")

    def set_radius(self, radius):
        """设置圆形半径"""
        self.radius = radius