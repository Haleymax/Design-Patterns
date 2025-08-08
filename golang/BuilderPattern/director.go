package BuilderPattern

import "golang/BuilderPattern/builder"

// Director 是建造者模式中的指挥者，负责使用建造者创建产品
type Director struct {
	builder builder.Builder
}

// NewDirector 创建一个新的指导者
func NewDirector(b builder.Builder) *Director {
	return &Director{
		builder: b,
	}
}

// Construct 指导建造过程
func (d *Director) Construct() builder.Product {
	return d.builder.
		SetWheels().
		SetSeats().
		SetStructure().
		GetVehicle()
}

// SetBuilder 设置具体的建造者
func (d *Director) SetBuilder(b builder.Builder) {
	d.builder = b
}
