#! bin/user/env python3

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
slot = int()

# append list with fruit added from user
def add_fruit():
    new_fruit = input("Add another fruit to the list ")
    fruit.append(new_fruit)

# return the fruit name along with the position in the list
def what_number(num):
    num = int(input("Enter a number to show the fruit from the list: "))
    if num > len(fruit) or num == 0:
        print("The number is out of range, try again.")
        what_number(num)
    else:
        print(num, ":", fruit[(num - 1)])

def show_list(seq):
    print("Your list of fruit: ", seq, "\n")

# Series1
print("Start of Series1: ")
show_list(fruit)
add_fruit()
show_list(fruit)
what_number(slot)
add_fruit = ["Cherries"]
new_fruit_list = add_fruit + fruit
show_list(new_fruit_list)
new_fruit_list.insert(0, "Pineapples")
show_list(new_fruit_list)
p_fruit = []
for item in new_fruit_list:
    if item[0] == 'P':
        p_fruit.append(item)
print(p_fruit, "\n")

# Series2
print("Start of Series2: ")
show_list(new_fruit_list)
new_fruit_list.remove(new_fruit_list[-1])
show_list(new_fruit_list)
temp = input("Which fruit would you like to delete? ")
while temp not in new_fruit_list:
    temp = input("Which fruit would you like to delete? ")
new_fruit_list.remove(temp)
show_list(new_fruit_list)

# Series3
print("Start of Series3: ")
copy_fruit = fruit[:]
for item in copy_fruit[:]:
    answer = input(f"Do you like {item.lower()}? (yes or no) ")
    while answer.lower() not in ['yes', 'no']:
        answer = input("Please enter 'yes or no.' ")
    if answer == 'no':
        copy_fruit.remove(item)
print(copy_fruit, "\n")

# Series4
copy_fruit = []
for item in fruit[:]:
    copy_fruit.append(item[::-1])
copy_fruit.remove(copy_fruit[-1])
print(copy_fruit)
print(fruit)