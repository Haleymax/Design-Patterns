package AbstractFactory

import "fmt"

func createFurnitureSet(factory FurnitureFactory) {
	chair := factory.CreateChair()
	sofa := factory.CreateSofa()
	coffeeTable := factory.CreateCoffeeTable()

	fmt.Println("=== 家具套装展示 ===")
	fmt.Println("椅子：", chair.SitOn(), "| 风格：", chair.Style())
	fmt.Println("沙发：", sofa.LieOn(), "| 风格：", sofa.Style())
	fmt.Println("咖啡桌：", coffeeTable.PutOn(), "| 风格：", coffeeTable.Style())
	fmt.Println("===================")
}

func Demo() {
	fmt.Println("=== 现代风格家具套装 ===")
	modernFactory := NewModernFurnitureFactory()
	createFurnitureSet(modernFactory)

	fmt.Println("=== 古典风格家具套装 ===")
	classicFactory := NewClassicFurnitureFactory()
	createFurnitureSet(classicFactory)
}
