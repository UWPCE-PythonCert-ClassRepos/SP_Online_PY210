#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 17:31:49 2019

@author: humberto gonzalez
"""

### List Lab ###

# Series 1

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)

response = input('Please type in the name of a fruit: ')

fruit_list = fruit_list + [response]
print(fruit_list)

n = len(fruit_list)
response = input('Please choose a number between 1 and {}: '.format(n))
print('{} = {}'.format(response,fruit_list[int(response)-1]))

new_fruit = 'Pineapples'
fruit_list = [new_fruit] + fruit_list
print()
print(fruit_list)

new_fruit = 'Watermelons'
fruit_list.insert(0,new_fruit)
print()
print(fruit_list)

print()
print('These are all fruits within the list that begin with P')
for fruit in fruit_list:
    if fruit[0]=='P' or fruit[0]=='p':
        print(fruit)

series1_list = fruit_list

# Series 2
series2_list = series1_list

print()
print(series2_list)

print()
series2_list = series2_list[:-1]
print(series2_list)

print()
response = input('Please choose a fruit from the list: ')
while response not in series2_list:
    response = input('Please choose a fruit from the list: ')
series2_list.remove(response)
print()
print(series2_list)


# Series 3
series3_list = series1_list

for fruit in series3_list:
    answers = ['No', 'no', 'Yes', 'yes', 'n', 'N', 'y', 'Y']
    dislike = ['No', 'no', 'n', 'N']
    response = input('Do you like {}? (y/n) '.format(fruit.lower()))
    while response not in answers:
        print('Please type in either yes or no')
        response = input('Do you like {}? (y/n) '.format(fruit))
    if response in dislike:
        series3_list.remove(fruit)

print()
print(series3_list)


# Series 4
series4_list = series1_list
new_list = []

for i in range(len(series4_list)):
    fruit = series4_list[i]
    new_list += [fruit[::-1]]

series4_list = series4_list[:-1]

print()
print(series4_list)
print()
print(new_list)







        

