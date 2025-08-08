// Package builder 建造者接口定义了一个产品创建的各个步骤
package builder

// Builder 接口定义了创建一个产品的各个步骤
type Builder interface {
	SetWheels() Builder    // 设置轮子
	SetSeats() Builder     // 设置座位
	SetStructure() Builder // 设置结构
	GetVehicle() Product   // 获取最终产品
}

// Product 是产品接口
type Product interface {
	Show() string // 展示产品信息
}
