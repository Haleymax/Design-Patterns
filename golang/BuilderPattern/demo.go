package BuilderPattern

import (
	"fmt"
	"golang/BuilderPattern/builder"
)

func Demo() {
	// 创建一个汽车建造者实例
	carBuilder := builder.NewCarBuilder()

	// 创建一个指导者实例，并传入汽车建造者
	director := NewDirector(carBuilder)
	car := director.Construct()
	fmt.Println(car.Show())

	// 创建一个房屋建造者实例
	houseBuilder := builder.NewHouseBuilder()
	director.SetBuilder(houseBuilder)
	house := director.Construct()
	fmt.Println(house.Show())

	// 也可以直接使用建造者而不通过指导者
	manualCar := builder.NewCarBuilder().
		SetWheels().
		SetSeats().
		SetStructure().
		GetVehicle()
	fmt.Println("\nManually built car:")
	fmt.Println(manualCar.Show())

}
