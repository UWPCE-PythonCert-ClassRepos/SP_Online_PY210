'''
Andrew Garcia
List Lab
6/15/19
'''

#!/usr/bin/env python3

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)


# Sequence 1
#print('\n' +'-------SEQUENCE 1-------')
# add new fruit to list
new_fruit = input("Add a fruit to the list: ")
fruit_list.append(new_fruit.title())
print(fruit_list)

# Print a fruit based on index input
fruit_number = int(input("Pick a number between 1 and " + str(len(fruit_list)) + ": "))
fruit_index = fruit_number - 1
print("You picked number {}, which means you picked {} \n".format(fruit_number, fruit_list[fruit_index]))

# Add two new fruits to beginning of list
new_fruit2 = input("Add a fruit to the list: ")
fruit_list = [new_fruit2.title()] + fruit_list
print(fruit_list, '\n')


new_fruit3 = input("Add a fruit to the list: ")
fruit_list.insert(0, new_fruit3.title())
print(fruit_list)

# Print fruits starting with P
print('\n' + "The fruits in your list that start with P are:")
for item in fruit_list:
    if 'P' in item[0]:
        print(item)



# Sequence 2
print('\n' + '-------SEQUENCE 2-------')
new_list = fruit_list.copy()

# Remove last item from list
print(new_list)
new_list.pop(-1)
print(new_list)

# Remove item from list based on user input
def removing_fruit(remove_fruit):
    if remove_fruit.title() in new_list:
        new_list.remove(remove_fruit.title())
    return new_list


remove_fruit = input('Which fruit would you like to remove?: ')
print(removing_fruit(remove_fruit))



# Sequence 3
print('\n' +'-------Sequence 3-------')


def find_favorite_fruits(list):
    favorites_list = []
    for item in list:
        while True:
            answer = input("Do you like {} ?: [Yes/No] ".format(item.lower()))
            if answer.lower() == 'no':
                break
            elif answer.lower() == 'yes':
                favorites_list += [item]
                break
            elif answer.lower() != 'yes' or 'no':
                print('That is not a valid answer.')
    return favorites_list


new_list = fruit_list.copy()
favorites = find_favorite_fruits(new_list)
print('You like the following fruits: \n', favorites)



# Sequence 4
print('\n' +'-------Sequence 4-------')
new_list = fruit_list.copy()


def reverse_fruits(list):
    reversed_list = []
    for item in list:
        reversing = []
        reversing += item
        reversing.reverse()
        backwards = ''.join(reversing)
        reversed_list += [backwards]
    return reversed_list


reversed_list = reverse_fruits(new_list)
new_list.pop(-1)
print(new_list)
print(reversed_list)

input()
