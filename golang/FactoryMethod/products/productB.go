package products

import "fmt"

// ConcreteProductB 是具体的产品B实现
type ConcreteProductB struct {
	name  string
	price float64
}

// NewConcreteProductB 创建ConcreteProductB的实例
func NewConcreteProductB(name string, price float64) *ConcreteProductB {
	return &ConcreteProductB{
		name:  name,
		price: price,
	}
}

// GetName 实现Product接口的GetName方法
func (p *ConcreteProductB) GetName() string {
	return p.name
}

// Use 实现Product接口的Use方法
func (p *ConcreteProductB) Use() string {
	return fmt.Sprintf("Using product B: %s", p.name)
}

// GetPrice 实现Product接口的GetPrice方法
func (p *ConcreteProductB) GetPrice() float64 {
	return p.price
}
