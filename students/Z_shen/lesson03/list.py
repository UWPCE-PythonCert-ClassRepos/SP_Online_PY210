
'''Series 1'''

def print_current_list(list):
    return print('The Current Fruit List is',list)

def user_fruit_input():
    return input('Enter a New Fruit into the List: ').title()

def user_number_input():
    return int(input('Enter a number between 1 to {}: '.format(len(fruit))))

def display_number_fruit(number):
    return print(fruit[number-1])
fruit=['Apples','Pears','Oranges','Peaches']
fruit2=fruit[:]
fruit3=fruit[:]
fruit4=fruit[:]

print_current_list(fruit)

fruit.append(user_fruit_input())

print_current_list(fruit)

display_number_fruit((user_number_input()))

print('-'*80)
fruit= ['Grapes'] + fruit  #Add another fruit to the beginning of the list using “+” and display the list.
print('Add Grapes to the beginning of the list using “+” and display the list')
print_current_list(fruit)

print('-'*80)
fruit.insert(0,'Papaya') #Add another fruit to the beginning of the list using insert() and display the list.
print('Add Papaya to the beginning of the list using insert() and display the list.')
print_current_list(fruit)

print('-'*80)
P_fruit=[]

#Display all the fruits that begin with “P”,
for item in fruit:
    if item[0] == 'P':
        P_fruit.append(item)
print_current_list(P_fruit)


'''Series 2'''
print('Series 2')
input()
def remove_fruit():
    return input('Enter a name of fruit you want to remove: ')

print_current_list(fruit2)
fruit2.pop() #Remove the last fruit from the list.
print_current_list(fruit2)
print('-'*80)
Del_fruit = remove_fruit()
for item in fruit:
    if item == Del_fruit.title():
        fruit2.remove(item)
print_current_list(fruit2)
print()
print('-'*80)
# Bonus
fruit_double=fruit2
fruit_double=fruit_double*2
print('The list is doubled',fruit_double)
print('-'*80)
delete = remove_fruit()
while delete.title() not in fruit_double:
    print('Fruit not found in the list!!!!!'.title())
    delete = remove_fruit()
while delete.title() in fruit_double:
    fruit_double.remove(delete.title())
print_current_list(fruit_double)


'''SERIES 3'''
print('Series 3')
input()
fav_fruit=[]

for item in fruit3:
    answer = input('Do you like fruit {}? '.format(item.lower()))
    if str(answer.upper()) == 'YES':
        fav_fruit.append(item)
        print('Fruit add to your list')

    elif answer.upper() == 'NO':
        print('Fruit remove from your list')

    else:
        print("------------------")
        print('Please Enter Yes or No only!!!!')
        answer = input('Do you like fruit {}? '.format(item.lower()))

print_current_list(fav_fruit)



'''Series 4'''
print('Series 4')
input()
reversed_fruit=[]
for item in fruit4:
    reversed_fruit.append(item[::-1])
print(reversed_fruit)
print_current_list(fruit4) #print the original list
fruit4.pop()  #remove the last fruit from the original list
print_current_list(fruit4) # print the copy

