package AbstractFactory

// ModernChair 是现代风格的椅子的具体实现
type ModernChair struct{}

func (m *ModernChair) SitOn() string {
	return "坐在现代风格的椅子上，感受简约与舒适"
}

func (m *ModernChair) Style() string {
	return "现代风格"
}

// ModernSofa 是现代风格的沙发的具体实现
type ModernSofa struct{}

func (m *ModernSofa) LieOn() string {
	return "躺在现代风格的沙发上，线条简约"
}

func (m *ModernSofa) Style() string {
	return "现代风格"
}

// ModernCoffeeTable 是现代风格的咖啡桌的具体实现
type ModernCoffeeTable struct{}

func (m *ModernCoffeeTable) PutOn() string {
	return "在现代风格的咖啡桌上放置物品，桌面光滑"
}

func (m *ModernCoffeeTable) Style() string {
	return "现代风格"
}

// ClassicChair  是古典风格椅子的具体实现
type ClassicChair struct{}

func (c *ClassicChair) SitOn() string {
	return "坐在古典风格的椅子上，感受优雅与舒适"
}

func (c *ClassicChair) Style() string {
	return "古典风格"
}

// ClassicSofa 是古典风格沙发的具体实现
type ClassicSofa struct{}

func (c *ClassicSofa) LieOn() string {
	return "躺在古典风格的沙发上，感受优雅与奢华"
}

func (c *ClassicSofa) Style() string {
	return "古典风格"
}

// ClassicCoffeeTable 是古典风格咖啡桌的具体实现
type ClassicCoffeeTable struct{}

func (c *ClassicCoffeeTable) PutOn() string {
	return "在古典风格的咖啡桌上放置物品，感受精致工艺"
}

func (c *ClassicCoffeeTable) Style() string {
	return "古典风格"
}
