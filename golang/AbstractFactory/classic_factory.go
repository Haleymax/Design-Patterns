package AbstractFactory

// ClassicFurnitureFactory 是古典风格家具的工厂
// 实现了 FurnitureFactory 接口
type ClassicFurnitureFactory struct{}

// NewClassicFurnitureFactory 创建一个新的古典风格家具工厂实例
func NewClassicFurnitureFactory() FurnitureFactory {
	return &ClassicFurnitureFactory{}
}

// CreateChair 创建古典风格的椅子
func (c *ClassicFurnitureFactory) CreateChair() Chair {
	return &ClassicChair{}
}

// CreateSofa 创建古典风格的沙发
func (c *ClassicFurnitureFactory) CreateSofa() Sofa {
	return &ClassicSofa{}
}

// CreateCoffeeTable 创建古典风格的咖啡桌
func (c *ClassicFurnitureFactory) CreateCoffeeTable() CoffeeTable {
	return &ClassicCoffeeTable{}
}
