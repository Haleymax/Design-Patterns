// 汽车产品定义
package product

import "strconv"

// Car 是具体的产品:汽车
type Car struct {
	Wheels    int
	Seats     int
	Structure string
}

// Show 展示汽车的信息
func (c *Car) Show() string {
	return "This is a " + c.Structure +
		" with " + strconv.Itoa(c.Wheels) + " wheels and " +
		strconv.Itoa(c.Seats) + " seats."
}
