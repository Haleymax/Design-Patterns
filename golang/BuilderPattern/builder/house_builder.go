package builder

import "golang/BuilderPattern/product"

// 房屋建造者实现

// HouseBuilder 是具体的房屋建造者
type HouseBuilder struct {
	house *product.House
}

// NewHouseBuilder 创建一个新的房屋建造者
func NewHouseBuilder() *HouseBuilder {
	return &HouseBuilder{
		house: &product.House{},
	}
}

// SetWheels 房屋没有轮子，这里的实现为空
func (h *HouseBuilder) SetWheels() Builder {
	h.house.Wheels = 0 // 房屋通常没有轮子
	return h
}

// SetSeats 设置房屋的座位数量（假设房屋内的椅子数量）
func (h *HouseBuilder) SetSeats() Builder {
	h.house.Seats = 10 // 假设房屋有10个座位
	return h
}

// SetStructure 设置房屋的结构
func (h *HouseBuilder) SetStructure() Builder {
	h.house.Structure = "House"
	return h
}

// GetVehicle 返回构建好的房屋产品
func (h *HouseBuilder) GetVehicle() Product {
	return h.house
}
