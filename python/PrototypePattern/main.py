from PrototypePattern.shape_cache import ShapeCache


def demonstrate_prototype():
    """
    演示原型模式的使用
    """
    # 初始化原型缓存
    print("Loading shape prototypes...")
    ShapeCache.load_cache()

    # 显示所有可用原型
    print("\nAvailable prototypes:")
    prototypes = ShapeCache.get_all_prototypes()
    for shape_id, shape_type in prototypes.items():
        print(f"ID: {shape_id}, Type: {shape_type}")

    # 通过克隆创建新对象
    print("\nCloning shapes...")
    shape_to_clone = ["1", "2", "3"]

    for shape_id in shape_to_clone:
        cloned_shape = ShapeCache.get_shape(shape_id)
        cloned_shape.draw()

        # 修改克隆对象的属性以证明它是新对象
        if cloned_shape.get_type() == "Circle":
            cloned_shape.set_radius(15)
        elif cloned_shape.get_type() == "Square":
            cloned_shape.set_side(20)
        elif cloned_shape.get_type() == "Rectangle":
            cloned_shape.set_dimensions(15, 25)

        print("After modification:")
        cloned_shape.draw()

        # 获取原始原型进行比较
        original = ShapeCache.get_shape(shape_id)
        print(f"Original shape: {original}")
        original.draw()
    else:
        print(f"\nShape with ID {shape_id} not found")

if __name__ == "__main__":
    demonstrate_prototype()