// Package AbstractFactory 定义抽象工厂模式中的接口
package AbstractFactory

// FurnitureFactory 是抽象工厂接口
// 声明了一系列创建产品的方法，这些方法返回抽象产品类型
type FurnitureFactory interface {
	CreateChair() Chair             // 创建椅子
	CreateSofa() Sofa               // 创建沙发
	CreateCoffeeTable() CoffeeTable // 创建咖啡桌
}

// Chair 是抽象椅子接口
type Chair interface {
	SitOn() string // 坐在椅子上的行为
	Style() string // 椅子的风格
}

// Sofa 是抽象沙发接口
type Sofa interface {
	LieOn() string // 躺在沙发上的行为
	Style() string // 沙发的风格
}

// CoffeeTable 是抽象咖啡桌接口
type CoffeeTable interface {
	PutOn() string // 在咖啡桌上放东西的行为
	Style() string // 咖啡桌的风格
}
