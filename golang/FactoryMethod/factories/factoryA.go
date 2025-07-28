package factories

import (
	"golang/FactoryMethod/interfaces"
	"golang/FactoryMethod/products"
)

// ConcreteFactoryA 是具体工厂A，负责创建产品A
type ConcreteFactoryA struct{}

// NewConcreteFactoryA 创建ConcreteFactoryA的实例
func NewConcreteFactoryA() *ConcreteFactoryA {
	return &ConcreteFactoryA{}
}

// CreateProduct 实现Factory接口的CreateProduct方法
// 创建具体产品A的实例
func (f *ConcreteFactoryA) CreateProduct(name string, price float64) interfaces.Product {
	return products.NewConcreteProductA(name, price)
}
