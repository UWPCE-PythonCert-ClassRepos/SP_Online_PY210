#!/usr/bin/env python3


list1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(list1)
response = input("Please type in another fruit: ")
list1.append(response)
print(list1)
number1 = input("please type a number (1-5): ")
integer1 = int(number1)
print(integer1)
print("Your number is {:s} which is fruit {:s}".
      format(number1, list1[integer1 - 1]))
list2 = ["Starfruit"]
list1 = list2 + list1
print(list1)
list1.insert(0, "Grapes")
print(list1)
for fruit in list1:
    if fruit[:1] == "P":
        print(fruit)


series2list = list1[:]
print(series2list)
series2list.pop()
print(series2list)
deleteFruit = input("Please type a fruit to delete: ")
series2list.remove(deleteFruit)

series3list = list1[:]
for fruit in list1[:]:
    like = input("Do you like {:s} ".format(fruit.lower()))
    while not (like == "yes" or like == "no"):
        like = input("Do you like {:s}".format(fruit.lower()))
    if like == "no":
        series3list.remove(fruit)
print(series3list)

series4list = []
for fruit in list1[:]:
    series4list.append(fruit[::-1])

list1.pop()
print(list1)
print(series4list)
