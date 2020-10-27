#!/usr/bin/env python3

##################################################
# Series 1
##################################################
fruits = ['Apples', 'Pears', 'Oranges','Peaches']
print(fruits)
new_fruit = input('Enter a new fruit: ')
fruits.append(new_fruit)
print(fruits)
ask_user = int(input('Enter a number between 1 and 5: '))
if ask_user > 5 or ask_user < 0:
    print('Enter a valid number: ')
    ask_user = int(input('Enter a number between 1 and 5: '))
    print('{0} is the number you entered and corresponding fruit you requested is: {1}'.format(str(ask_user), fruits[ask_user-1]))
else:
    print('{0} is the number you entered and corresponding fruit you requested is: {1}'.format(str(ask_user), fruits[ask_user-1]))
fruits[:] = ['Melons'] + fruits[:]
fruits.insert(0,'Banana')
for i in range(len(fruits)):
    if fruits[i][0].lower() == 'p':
        print(fruits[i])

##################################################
# Series 2
##################################################
fruits.pop()
print(fruits)
fruits = fruits * 2
del_fruit = input('Enter a fruit name to delete: ').title()
i, wrd_found = 0, False
while i < len(fruits):
    if fruits[i] == del_fruit:
        del fruits[i]
        wrd_found = True
    i += 1
if not wrd_found:
    print('You inputted a fruit which is not in the list.')
else:
    print('new list is: ', fruits)

##################################################
# Series 3
##################################################
del_list = []
for i in range(len(fruits)):
    prompt_check = True
    while prompt_check:
        prompt = input('Do you like {0}? '.format(fruits[i]).lower())
        if prompt == 'yes':
            prompt_check = False
        elif prompt == 'no':
            prompt_check = False
            del_list.append(fruits[i])
        else:
            print('Please enter yes or no only.')
fruits = [x for x in fruits if x not in del_list]
print(fruits)

##################################################
# Series 4
##################################################
new_fruits = []
for i in range(0, len(fruits)-1):
    new_fruits.append(fruits[i][::-1])
print('Copied list: ', new_fruits)
print('Original list: ', fruits)
