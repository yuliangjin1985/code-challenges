package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("Hello, World!")
	fmt.Println("1+1=", 1+1)
	fmt.Println("1/8=", 1/8)
	fmt.Println("1.0/8=", 1.0/8)
	var a string = "initial"
	b := "letterb"
	fmt.Println(a, b)
	const d = 3e20
	//Change d to string format to show all the digits

	//output 3000.000000
	fmt.Println(fmt.Sprintf("%f", 3e3))

	//output 3000
	fmt.Println(fmt.Sprintf("%d", int16(3e3)))

	fmt.Print(math.Sin(1))

	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	for i := range 5 {
		fmt.Println(i)
	}

	//
	for i := range "golang" {
		fmt.Println("golang"[i])
	}
}
