#!/usr/bin/env python3

#Series 1
fruitlist = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruitlist)

add_fruit = input("\nAnother fruit, perhaps? What would you like?\n")
fruitlist.append(add_fruit)
print(fruitlist)

number = int(input("\nPick a number from 1 to " + str(len(fruitlist)) + ".\n"))
print(number, ": ", fruitlist[number-1],"\n")

fruitlist = ["Guava"] + fruitlist
print(fruitlist)

fruitlist.insert(0, "Mango")
print(fruitlist)

for fruit in fruitlist:
	if fruit[0] == "P":
		print(fruit)


#Series 2
fruitlist2 = fruitlist[:]
print(fruitlist2)
del fruitlist2[-1]
print(fruitlist2)

#Series 2 bonus
fruitlist2 = fruitlist2*2

while True:
	try:
		xfruit = input("\nWhat fruit should we take away?\n")
		fruitlist2.index(xfruit)
		break
	except:
		print("Let's behave. Try another fruit!")

newfruitlist2 = [x for x in fruitlist2 if x != xfruit]
print(newfruitlist2)


#Series 3
fruitlist3 = fruitlist[:]

for fruit in fruitlist:
	while True:
		yn = input(f"Do you like {fruit.lower()}? (yes or no)\n")
		if yn != "yes" and yn != "no":
			print("Let's behave. Just type yes or no, please!\n")
			
		elif yn == "no":
			fruitlist3 = [x for x in fruitlist3 if x != fruit]
			break
		
		else:
			break

print(fruitlist3)


#Series 4
fruitlist4 = fruitlist[:]

for i, fruit in enumerate(fruitlist):
	fruitlist4[i]=fruit[::-1]

print(fruitlist[:-1])
print(fruitlist4)

input()
