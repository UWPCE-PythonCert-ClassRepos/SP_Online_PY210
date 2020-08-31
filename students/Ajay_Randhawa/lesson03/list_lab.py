#!/usr/bin/env python3
def Series1():
	list1 = ["Apples", "Pears", "Oranges", "Peaches"]
	print(list1)
	x = input("Name another fruit:")
	list1.append(x)
	print(list1)
	number = input("Type a number:")
	print(number)
	print(list1[int(number) -1])
	list1 = ["Guava"] + list1
	print(list1)
	list1.insert(0, "Grapes")
	print(list1)
	for i in list1:
		if i.startswith("P"):
			print(i)
