#!/usr/bin/env python3

#Series 1 tasks
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)

new_fruit = input('Please add another fruit: ')
fruit_list.append(new_fruit)
print('This is the new list of fruits: ' + str(fruit_list) + '\n')

fruit_idx = input('Please choose a number between 1-5: ')
fruit_idx = int(fruit_idx)
print(fruit_idx, fruit_list[fruit_idx - 1])

new_fruit2 = ['Mangos']
fruit_list2 = new_fruit2 + fruit_list
print('Adding Mangos to fruit list using "+": ' + str(fruit_list2) + '\n')

fruit_list2.insert(0, 'Nectarines')
print('Adding Nectarines to fruit list using ".insert": ' + str(fruit_list2) + '\n')

starts_with_P_list = []
for fruit in fruit_list2:
    if fruit.startswith('P'):
        starts_with_P_list.append(fruit)
print('All the fruits in the list that start with "P": ' + str(starts_with_P_list) + '\n')

#Series 2 tasks - Make shallow copy of list so can change it without affecting original
series2_fruit = fruit_list2[:]
print('List for the start of series 2: ' + str(series2_fruit) + '\n')
series2_fruit.pop(-1)
print('Removed last item from list: ' + str(series2_fruit) + '\n')
delete_fruit = input('Please choose a fruit to toss: ')
series2_fruit.remove(delete_fruit)
print(series2_fruit)

#Series 3 tasks
series3_fruit = fruit_list2[:]
print('This is the list for the start of series3: '+ str(series3_fruit) + '\n')

def customer_favorite():
    i = 0
    while i < len(series3_fruit):
        answer = input("Do you like " + series3_fruit[i].lower() + ': ')
        if answer.lower() == 'no':
            series3_fruit.pop(i)
        elif answer.lower() == 'yes':
            i = i + 1
        else:
            print('Please answer yes or no')
            continue

customer_favorite()

print("These are the fruits you like: " + str(series3_fruit))

#Series 4 tasks
series4_fruit = fruit_list2[:]
reversed_fruit = [x[::-1] for x in series4_fruit[::-1]]
print(str(fruit_list2[:-1]) + "\n" + str(reversed_fruit))
