package factories

import (
	"golang/FactoryMethod/interfaces"
	"golang/FactoryMethod/products"
)

// ConcreteFactoryB 是具体工厂B，负责创建产品B
type ConcreteFactoryB struct{}

// NewConcreteFactoryB 创建ConcreteFactoryB的实例
func NewConcreteFactoryB() *ConcreteFactoryB {
	return &ConcreteFactoryB{}
}

// CreateProduct 实现Factory接口的CreateProduct方法
// 创建具体产品B的实例
func (f *ConcreteFactoryB) CreateProduct(name string, price float64) interfaces.Product {
	return products.NewConcreteProductB(name, price)
}
