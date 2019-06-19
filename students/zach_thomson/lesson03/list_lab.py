#!/usr/bin/env python3

#Series 1 tasks
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)
new_fruit = input('Please add another fruit: ')
fruit_list.append(new_fruit)
print(fruit_list)
fruit_idx = input('Please choose a number between 1-5: ')
fruit_idx = int(fruit_idx)
print(fruit_idx, fruit_list[fruit_idx - 1])
new_fruit2 = ['Mangos']
fruit_list2 = new_fruit2 + fruit_list
print(fruit_list2)
fruit_list2.insert(0, 'Nectarines')
print(fruit_list2)
starts_with_P_list = []
for fruit in fruit_list2:
    if fruit.startswith('P'):
        starts_with_P_list.append(fruit)
print(starts_with_P_list)

#Series 2 tasks - Make shallow copy of list so can change it without affecting original
series2_fruit = fruit_list2[:]
print(series2_fruit)
series2_fruit.pop(-1)
print(series2_fruit)
delete_fruit = input('Please choose a fruit to toss: ')
series2_fruit.remove(delete_fruit)
print(series2_fruit)

#Series 3 tasks
