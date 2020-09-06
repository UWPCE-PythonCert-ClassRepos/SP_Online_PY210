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
def Series2():
	list2 = ["Apples", "Pears", "Oranges", "Peaches"]
	#Display the list
	print(list2)
	#REmove the last fruit from the list
	list2.pop()
	#Display the list
	print(list2)
	#Ask the user for a fruit to delete, find it and delete it
	#Bonus
	#only works for when the list is multiplied by less than or equal to 2.
	list2 = list2*2
	print(list2)
	count = 0
	while(count<2):
		delete = input("Name a fruit to be deleted from the list: ")
		for i in list2:
			if i == delete:
				list2.remove(delete)
				count = count +1
		if count < 2:
			print("No match found, try again: ")
	print(list2)
	"""
		Series3
	"""
def Series3():
	""" Ask the user "do you like Apples?" for every
	item in the list. 
	For each no delete the item from the list.
	For any answer that is not "yes" or "no". prompt the user
	to answer with one of those two values."""
	list3 = ["Apples", "Pears", "Oranges", "Peaches"]
	list3_copy = list3[0:]
	for i in list3:
		while(1):
			print("Do you like", i,"? (yes/no)")
			item = str(input())
			if item == "yes":
				pass
				break
			if item == "no":
				list3_copy.remove(i)
				break
			else:
				print("Answer with one of the two values 'yes' or 'no'")
				pass
	print(list3_copy)

def Series4():
	list4 = ["Apples", "Pears", "Oranges", "Peaches"]
	#Make a list with the contents of the original,
	#but, with all the letters in each item reversed.
	list4_new = [i[::-1] for i in list4]
	#Delete the last item of the original list.
	list4.pop()
	print(list4)
	print(list4_new)