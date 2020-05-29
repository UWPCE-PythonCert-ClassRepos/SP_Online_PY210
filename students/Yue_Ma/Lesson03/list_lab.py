#!/usr/bin/env python3

# series 1

# dot1
list_fruit1 = ['Apples', 'Pears', 'Oranges', 'Peaches']

# dot2
print(list_fruit1)

# dot3
response = input('Enter a fruit name:')
list_fruit1.append(response)

# dot4
print(list_fruit1)

# dot5
number = int(input('Enter a number between 1-5:'))
print(number, list_fruit1[number - 1])

# dot6
fruit = ['Watermelon']
list_fruit1 = list_fruit1 + fruit
print(list_fruit1)

# dot7
list_fruit1.insert(0, 'Dragonfruit')
print(list_fruit1)

# dot 8
for item in list_fruit1:
    if item[0] == 'P':
        print(item)

# Series 2

list_fruit2 = ['Apples', 'Pears', 'Oranges', 'Peaches']
# dot1
print(list_fruit2)

# dot2
list_fruit2.pop(0)

# dot3
print(list_fruit2)

# dot4
delete = input("Please enter a fruit name that you want to delete:")
if delete in list_fruit2:
    list_fruit2.remove(delete)
    print(list_fruit2)
else:
    print('Not in the list')
# Series 3
list_fruit3 = ['Apples', 'Pears', 'Oranges', 'Peaches']
result = []
for i in range(0, len(list_fruit3)):
    like = input('Do you like ' + list_fruit3[i] + '? (yes/ no)')
    while like.lower() != 'yes' and like.lower() != 'no':
        like = input('Do you like ' + list_fruit3[i] + '? (yes/ no)')
    if like.lower() == 'no':
        result.append(list_fruit3[i])
print(result)

# Series 4
list_fruit4_1 = ['Apples', 'Pears', 'Oranges', 'Peaches']
list_fruit4_2 = ['Apples', 'Pears', 'Oranges', 'Peaches']
for i in range(0, len(list_fruit4_1)):
    list_fruit4_1[i] = list_fruit4_1[i][::-1]
list_fruit4 = list_fruit4_2.pop(-1)
print(list_fruit4_1)
print(list_fruit4_2)
