package FactoryMethod

import (
	"fmt"
	"golang/FactoryMethod/factories"
	"golang/FactoryMethod/interfaces"
)

func Demo() {
	// 创建工厂A
	factoryA := factories.NewConcreteFactoryA()
	// 使用工厂A创建产品A
	productA := factoryA.CreateProduct("Product A", 19.99)
	printProductInfo(productA)

	// 创建工厂B
	factoryB := factories.NewConcreteFactoryB()
	// 使用工厂B创建产品B
	productB := factoryB.CreateProduct("Product B", 29.99)
	printProductInfo(productB)
}

// printProductInfo 打印产品信息
func printProductInfo(p interfaces.Product) {
	fmt.Println("Product Name:", p.GetName())
	fmt.Println("Product Price:", p.GetPrice())
	fmt.Println("Product Use:", p.Use())
	fmt.Println("-----------------------")
}
