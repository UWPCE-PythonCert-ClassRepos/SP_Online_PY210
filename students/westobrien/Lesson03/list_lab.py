#!/usr/bin/env python3
list1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(list1)
response = input("Please type in another fruit: ")
list1.append(response)
print(list1)
number = input("please type a number (1-4): ")
print("Your number is {number} which is fruit # {}".format(list1[number - 1]))
