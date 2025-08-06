package AbstractFactory

// ModernFurnitureFactory 是现代风格家具的工厂
// 实现了 FurnitureFactory 接口
type ModernFurnitureFactory struct{}

// NewModernFurnitureFactory 创建一个新的现代风格家具工厂实例
func NewModernFurnitureFactory() FurnitureFactory {
	return &ModernFurnitureFactory{}
}

// CreateChair 创建现代风格的椅子
func (m *ModernFurnitureFactory) CreateChair() Chair {
	return &ModernChair{}
}

// CreateSofa 创建现代风格的沙发
func (m *ModernFurnitureFactory) CreateSofa() Sofa {
	return &ModernSofa{}
}

// CreateCoffeeTable 创建现代风格的咖啡桌
func (m *ModernFurnitureFactory) CreateCoffeeTable() CoffeeTable {
	return &ModernCoffeeTable{}
}
