// Package builder 汽车建造者实现
package builder

import "golang/BuilderPattern/product"

// CarBuilder 是具体的建造者:汽车建造者
type CarBuilder struct {
	car *product.Car
}

// NewCarBuilder 创建一个新的汽车建造者实例
func NewCarBuilder() *CarBuilder {
	return &CarBuilder{car: &product.Car{}}
}

// SetWheels 设置汽车的轮子数量
func (c *CarBuilder) SetWheels() Builder {
	c.car.Wheels = 4
	return c
}

// SetSeats 设置汽车的座位数量
func (c *CarBuilder) SetSeats() Builder {
	c.car.Seats = 5
	return c
}

// SetStructure 设置汽车的结构
func (c *CarBuilder) SetStructure() Builder {
	c.car.Structure = "Car"
	return c
}

// GetVehicle 返回构建好的汽车产品
func (c *CarBuilder) GetVehicle() Product {
	return c.car
}
