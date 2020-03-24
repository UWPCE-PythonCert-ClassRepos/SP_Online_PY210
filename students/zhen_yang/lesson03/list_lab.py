#####################
# List Lab Exercise #
#####################

#####################
# Series 1
#####################
# 1.1 Create a list 
my_list = ['Apples','Pears','Oranges','Peaches']
print(f"My fruit list is: {my_list}.")

# 1.2 Add item to the list 
new_item = input("Please input another fruit: ")
my_list.append(new_item)
print(f"1. My updated fruit list is: {my_list}.")

# 1.3 Ask user a number and display the number back and 
# the fruit corresponding to that number  
input_str = input(f"Please input a number within range: [1:{len(my_list)}] ")
input_num = int(input_str) 
if input_num >= 1 and input_num <= len(my_list): 
    print(f"Input Number is: {input_num} and the corresponding fruit is: {my_list[input_num-1]}")
else:
    print("Input Number is out of list range!")
    exit()

# 1.4 Add another fruit to the beginning of the list using '+' 
new_fruit = ['Watermelon']
my_list = new_fruit + my_list
print(f"Add item to list using + : {my_list}.")

# 1.5 Add another fruit to the beginning of the list using insert() 
my_list.insert(0,'Avocado')
print(f"Add item to list using insert(): {my_list}.")

# 1.6 Display all the fruits that begin with "P" using a for loop
for i in my_list:
    if i[0:1] == 'P':
        print(f"Fruit Starts with letter P: {i}")


#####################
# Series 2 
#####################
# 2.1 Display the list created in Series 1
print(f"My fruit list created in Series 1: {my_list}")

# copy a list for latter use
backup_list = my_list[:]

# 2.2 Remove the last fruit from the list
my_list.pop()

# 2.3 Display the list
print(f"My fruit list after remove the last fruit: {my_list}")

# 2.4 Ask user for a fruit to delete, find it and delete it.
input_str = input(f"Please input a fruit name: ")
for i in my_list[:]: # iterate over a copy and mutate the original list
    if i == input_str:
        my_list.remove(i) 
        print(f"Found the fruit: {input_str}.")
        print(f"Updated list:{my_list}")
        break
else:
    print(f"Couldn't find the fruit: {input_str} from the list.")


# 2.5 Bonus: Multiply the list times two. 
# Keep asking until a match is found. Once found, delete all occurrences 

# multiply the list by times two
my_list = backup_list * 2
print(f"Doubled list: {my_list}.")

# Get the input fruit name
input_str = input(f"Please input a fruit name that you want to delete: ")
# Count the number of times that the fruit name appears in the list
my_count = my_list.count(input_str)

# if the input fruit does not appear in the list,
# we will keep asking a name for a fruit.
while my_count == 0:
    input_str = input("Can't find the name from the list. Please input another name: ")
    my_count = my_list.count(input_str)
print(f"Found the fruit:{input_str} appears in the list {my_count} times.")


# Found the fruit from the list, then we delete all the occurrences
# Iterate the total number of occurances, then get the index of the 
# first occurence of the fruit in the list and remove it by pop()
for i in range(my_count):
      the_index = my_list.index(input_str)
      my_list.pop(the_index)

print(f"Remove all the fruit:{input_str} from the list.")
print(f"Updated list {my_list}.")



#####################
# Series 3 
#####################






