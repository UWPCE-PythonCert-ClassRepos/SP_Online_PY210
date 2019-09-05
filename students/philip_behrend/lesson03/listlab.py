# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:45:05 2019

Author: Philip Behrend
"""

print("###Series 1####")
fruit = ['Apples','Oranges','Pears','Peaches']
print(fruit)
response = input("Gimme a different fruit: ")
fruit.append(response)
print(fruit)
num_response = 0
while (num_response < 1) or (num_response > 5):
    num_response = int(input("A number between 1 and 5 please: "))
print(fruit[num_response-1])
fruit = ['Grapes']+fruit
fruit.insert(1,'Papaya')
input("Press any key to continue...")

print("###Series 2####")
fruit = ['Apples','Oranges','Pears','Peaches']
print(fruit)
fruit.pop()
print(fruit)
del_fruit = ''
while del_fruit not in fruit:
    del_fruit = input("Delete a fruit: ")
fruit.remove(del_fruit)
print(fruit)
input("Press any key to continue...")

print("###Series 3####")
fruit = ['Apples','Oranges','Pears','Peaches']
print(fruit)
ask_user = []
preference = []
response = ''
for i,val in enumerate(fruit):
    while response not in ('yes', 'no'):
        response = input("Do you like {}? ".format(val.lower())).lower()
    preference.append(response)
    response = ''
no_index = [i for i,x in enumerate(preference) if x == 'no']
[fruit.pop(i) for i in no_index]
print(fruit)
input("Press any key to continue...")

print("###Series 4####")
fruit = ['Apples','Oranges','Pears','Peaches']
fruit_mod = [i[::-1] for i in fruit]
del fruit_mod[-1]
print(fruit,'\n', fruit_mod)
input("Press any key to continue...")

