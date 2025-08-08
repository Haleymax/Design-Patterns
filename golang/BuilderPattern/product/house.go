package product

import "strconv"

// 房屋产品定义

type House struct {
	Wheels    int
	Seats     int
	Structure string
}

// Show 展示房屋的信息
func (h *House) Show() string {
	return "This is a " + h.Structure +
		" with " + strconv.Itoa(h.Wheels) + " wheels and " +
		strconv.Itoa(h.Seats) + " seats."
}
