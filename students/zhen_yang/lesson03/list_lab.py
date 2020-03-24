#####################
# List Lab Exercise #
#####################

#####################
# Series 1
#####################
# Create a list 
my_list = ['Apples','Pears','Oranges','Peaches']
print(f"My fruit list is: {my_list}.")

# Add item to the list 
new_item = input("Please input another fruit: ")
my_list.append(new_item)
print(f"1. My updated fruit list is: {my_list}.")

# Ask user a number and display the number back and 
# the fruit corresponding to that number  
input_str = input(f"Please input a number within range: [1:{len(my_list)}] ")
input_num = int(input_str) 
if input_num >= 1 and input_num < len(my_list): 
    print(f"Input Number is: {input_num} and the corresponding fruit is: {my_list[input_num-1]}")
else:
    print("Input Number is out of list range!")
    exit()

# Add another fruit to the beginning of the list using '+' 
new_fruit = ['Watermelon']
my_list = new_fruit + my_list
print(f"Add item to list using + : {my_list}.")

# Add another fruit to the beginning of the list using insert() 
my_list.insert(0,'Avocado')
print(f"Add item to list using insert(): {my_list}.")

# Display all the fruits that begin with "P" using a for loop
for i in my_list:
    if i[0:1] == 'P':
        print(f"Fruit Starts with letter P: {i}")


