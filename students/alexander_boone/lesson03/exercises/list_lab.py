#!/usr/bin/env python3

# Note: Unsure if list from beginning or end of series 1 should be used for later series. 
#       I reused the list from the end of series 1 in later series.

# --------------------------------------------------- SERIES 1 -----------------------------------------------------
print("------------------ SERIES 1 ------------------")
l = ["Apples", "Pears", "Oranges", "Peaches"]
print(l)

l.append(input("Enter the name of another fruit: "))
print(l)

# ask user for number and display corresponding list element (starting index of 1)
user_choice = int(input("Enter a number: ")) - 1
print(l[user_choice])

# add item to beginning of list
l = [input("Enter the name of another fruit: ")] + l[:]
print(l)

# add another item to beginning of list
l.insert(0, input("Enter the name of another fruit: "))
print(l)

# display items that begin with a p
for fruit in l:
    if fruit[0] == "P" or fruit[0] == "p":
        print(fruit)

series1_list = list(l)
# --------------------------------------------------- SERIES 2 -----------------------------------------------------
print("------------------ SERIES 2 ------------------")
# display list
l = list(series1_list)
print(l)

# remove last element from list
l.pop()
print(l)

# prompt user for element to delete
fruit_delete = input("Enter the name of a fruit to remove from the list: ")
l.remove(fruit_delete)
print(l)

# --------------------------------------------------- SERIES 3 -----------------------------------------------------
print("------------------ SERIES 3 ------------------")
l = list(series1_list)
print(l)
possible_answers = ["yes", "Yes", "no", "No"]
removed_fruit = []
for fruit_item in l:
    
    like_fruit = ""

    # loop until yes or no is input by user
    while like_fruit not in possible_answers:
        like_fruit = input(f"Do you like {fruit_item}? (Yes/No) ")
    
    # if no, add fruit_item to removed_fruit list
    if like_fruit == "no" or like_fruit == "No":
        removed_fruit.append(fruit_item)

# constructs new list by removing removed_fruit list items from l
l = [x for x in l if x not in removed_fruit]
print(l)

# --------------------------------------------------- SERIES 4 -----------------------------------------------------
print("------------------ SERIES 4 ------------------")
l = list(series1_list)

# reverse string in each item of list
for item in l:
    l[l.index(item)] = item[::-1]

# remove last item from series1_list, print it, and print the original series1_list
series1_list.pop()
print(series1_list)
print(l)