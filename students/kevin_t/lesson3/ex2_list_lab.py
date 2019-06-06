#Create list of fruit and print it
my_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print (my_list)

#Ask user to add another fruit. Make it title cased and add it to the end. Display the list
my_list.append((input('What fruit would you like to add?' )).title())
print (my_list)

#Ask the user for a number, display the number and the fruit corresponding to the number.
#1 is first basis. Truncate input, check that the number is in range.
while True:
    user_num = int(input('Which number in the list would you like to pull? '))
    if user_num - 1 in range(len(my_list)):
        break
print('The fruit in position {} is {}'.format(user_num, my_list[user_num-1]))

#Add another fruit to the beginning using '+', display the list
my_list = ['Papayas'] + my_list
print (my_list)

#Add another fruit to the beginning using 'insert()', display the list
my_list.insert(0,'Mangos')
print (my_list)

#Display all fruits that begin with "P" using a 'for' loop
for fruit in my_list:
    if fruit[0] == 'P':
        print (fruit)
print (my_list)

#Remove the last fruit from the list, display the list
del my_list[-1]
print (my_list)

#Ask the user for a fruit to delete, verify the fruit is in the list.
#Delete all occurences of that fruit, display the list
while True:
    user_del = input('Which fruit would you like to delete? ')
    if user_del.title() in my_list:
        break
while user_del in my_list:
    my_list.remove((user_del).title())
print (my_list)

#Make a copy of the list, ask user if they like each fruit.
#Check that the answer is 'yes' or 'no', ask again if not.
#If no, delete that fruit from the list. Display the list
copy_my_list = my_list[:]
for fruit in copy_my_list:
    while True:
        fruit_preference = input('Do you like {}?'.format(fruit.lower()))
        if fruit_preference.lower() == 'yes' or fruit_preference.lower() == 'no':
            break
    if fruit_preference.lower() == 'no':
        my_list.remove(fruit)
print (my_list)

#Make a new list with the contents of the original, but reverse the letters in each
my_new_list = my_list[:]
for i,fruit in enumerate(my_new_list):
    my_new_list[i] = my_new_list[i][::-1]
print (my_new_list)

#Delete last item of original list. Display both.
my_list.remove(my_list[-1])
print(my_list)
print(my_new_list)