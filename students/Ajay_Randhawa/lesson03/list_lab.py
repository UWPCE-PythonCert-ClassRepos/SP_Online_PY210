#!/usr/bin/env python3
def Series1():
	#Create list
	list1 = ["Apples", "Pears", "Oranges", "Peaches"]
	#Display list
	print(list1)
	#Ask the user for another fruit and add it to the list
	x = input("Name another fruit:")
	list1.append(x)
	#Display the list
	print(list1)
	#Ask the user for a number
	number = input("Type a number:")
	#Display the number
	print(number)
	#Display the fruit corresponding to the input
	print(list1[int(number) -1])
	#Add another fruit to the beginning fo the list using "+"
	list1 = ["Guava"] + list1
	#Display the list
	print(list1)
	#Add another fruit to the beginning of the list using 'insert()'
	list1.insert(0, "Grapes")
	#Display the list
	print(list1)
	#Display all fruits that begin iwth "P", using a for loop.
	for i in list1:
		if i.startswith("P"):
			print(i)
	"""

	Series 2


	"""
	#Display the list
	print(list1)
	#REmove the last fruit from the list
	list1.pop()
	#Display the list
	print(list1)
	#Ask the user for a fruit to delete, find it and delete it
	#Bonus
	#only works for when the list is multiplied by less than or equal to 2.
	list1 = list1*2
	print(list1)
	count = 0
	while(count<2):
		delete = input("Name a fruit to be deleted from the list: ")
		for i in list1:
			if i == delete:
				list1.remove(delete)
				count = count +1
		if count < 2:
			print("No match found, try again: ")
	print(list1)