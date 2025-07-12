from PrototypePattern.shapes.circle import Circle
from PrototypePattern.shapes.rectangle import Rectangle
from PrototypePattern.shapes.square import Square


class ShapeCache:
    """
    原型管理器类
    负责创建、存储和管理原型对象
    提供获取克隆对象的接口
    """

    _shape_map = {}  # 类变量，存储原型对象

    @classmethod
    def get_shape(cls, shape_id):
        """
        根据ID获取形状的克隆
        参数：
            shape_id：要获取的形状id
        返回：
            克隆后的形状对象，如果ID不存子则返回None
        """
        cached_shape = cls._shape_map.get(shape_id)
        if cached_shape:
            return cached_shape.clone()
        return None

    @classmethod
    def load_cache(cls):
        """
        初始化原型缓存
        创建并存储各种形状的原型实例
        """
        # 创建圆形原型
        circle = Circle()
        circle.set_id("1")
        circle.set_radius(5)
        cls._shape_map[circle.get_id()] = circle

        # 创建正方形原型
        square = Square()
        square.set_id("2")
        square.set_side(10)
        cls._shape_map[square.get_id()] = square

        # 创建矩形原型
        rectangle = Rectangle()
        rectangle.set_id("3")
        rectangle.set_dimensions(8, 12)
        cls._shape_map[rectangle.get_id()] = rectangle

    @classmethod
    def get_all_prototypes(cls):
        """
        获取所有原型信息（用于调试）
        返回：
            原型ID和类型的字典
        """
        return {id: shape.get_type() for id, shape in cls._shape_map.items()}