package products

import "fmt"

// ConcreteProductA 是具体的产品A实现
type ConcreteProductA struct {
	name  string
	price float64
}

// NewConcreteProductA 创建ConcreteProductA实例
func NewConcreteProductA(name string, price float64) *ConcreteProductA {
	return &ConcreteProductA{
		name:  name,
		price: price,
	}
}

// GetName 实现Product接口的GetName方法
func (p *ConcreteProductA) GetName() string {
	return p.name
}

// Use 实现Product接口的Use方法
func (p *ConcreteProductA) Use() string {
	return fmt.Sprintf("Using product A: %s", p.name)
}

// GetPrice 实现Product接口的GetPrice方法
func (p *ConcreteProductA) GetPrice() float64 {
	return p.price
}
