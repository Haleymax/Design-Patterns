package interfaces

// Product 定义了产品的通用接口
// 所有具体产品都需要实现这个接口
type Product interface {
	// GetName 返回产品名称
	GetName() string

	// Use 使用产品的方法
	Use() string

	// GetPrice 返回产品价格
	GetPrice() float64
}
