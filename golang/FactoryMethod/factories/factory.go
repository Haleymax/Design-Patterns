package factories

import "golang/FactoryMethod/interfaces"

// Factory 是工厂接口
// 定义了创建产品的方法
type Factory interface {
	// CreateProduct 创建产品的方法
	// name: 产品名称
	// price: 产品价格
	CreateProduct(name string, price float64) interfaces.Product
}
