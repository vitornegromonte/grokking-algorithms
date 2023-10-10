package main

import "fmt"

func binarySearch(list []int, target int) int {
	low := 0
	high := len(list) - 1

	for low <= high {
		mid := (low + high) / 2

		if list[mid] == target {
			return mid
		}
		if list[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1
}

func main() {
	sample_list := []int{1, 3, 5, 7, 9}

	fmt.Println(binarySearch(sample_list, 3))  // => 1
	fmt.Println(binarySearch(sample_list, -1)) // => -1 (no value -1 in sample_list)
}
