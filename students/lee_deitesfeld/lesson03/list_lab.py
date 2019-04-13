#!/usr/bin/env python3

#------------ series 1 -------------#
print('\n SERIES 1')
lst_fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(lst_fruit)
frt_add_end = input("What fruit would you like to add?")
lst_fruit.append(frt_add_end)
print(lst_fruit)
to_display = input("Please enter a number: ")
to_display = int(to_display)
print(to_display, ":", lst_fruit[to_display-1])
frt_add_begin = input("What fruit would you like to add?")
lst_fruit = [frt_add_begin] + lst_fruit
print(lst_fruit)
frt_add_insert = input("What fruit would you like to add?")
lst_fruit.insert(0,frt_add_insert)
print(lst_fruit)
for fruit in lst_fruit:
    if fruit.startswith('P'):
        print(fruit)

#------------ series 2 -------------#
print('\n SERIES 2')
print(lst_fruit)
del lst_fruit[-1]
print(lst_fruit)
lst_double = lst_fruit*2
frt_delete = input("Which fruit would you like to remove?")
for fruit in lst_double:
    if fruit != frt_delete:
        frt_delete = input("Once again?")
    elif fruit == frt_delete:
        break
for fruit in lst_double:
    if fruit == frt_delete:
        lst_double.remove(frt_delete)
print(lst_double)

#------------ series 3 -------------#
print('\n SERIES 3')
print(lst_fruit)
#loop through reversed list so items aren't skipped if user enters 'no'
for fruit in reversed(lst_fruit):
    likefruit = input("Do you like " + fruit.lower() + "?")
    if likefruit == 'yes':
        continue
    elif likefruit == 'no':
        lst_fruit.remove(fruit)
    else:
        print("Please enter yes / no")
        input("Do you like " + fruit.lower() + "?")
print(lst_fruit)

#------------ series 4 -------------#
print('\n SERIES 4')
lst_to_be_rev = ['Apples', 'Pears', 'Oranges', 'Peaches']
#new list to append reversed items to
lst_rev = []
for fruit in lst_to_be_rev:
    fruit_rev = fruit[::-1]
    lst_rev.append(fruit_rev)
print(lst_rev)

print(lst_to_be_rev)
del lst_to_be_rev[-1]
print(lst_to_be_rev)
