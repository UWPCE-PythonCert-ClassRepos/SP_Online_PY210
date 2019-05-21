#!/usr/bin/env python3

# Series 1
a_list = ["Apples", "Pears","Oranges", "Peaches"]

def series_1(a_list):
    print(a_list)
    fruit = input("Enter a fruit to add to the list: ")
    a_list.append(fruit)
    print(a_list)
    number = input("Enter a number: ")
    print("Number entered " + number + " corresponding item in the list is " + a_list[int(number) - 1])
    a_list = ["Banana"] + a_list
    print(a_list)
    a_list.insert(0, "Plums")
    print(a_list)

    for i in a_list:
        if i.startswith("P"):
            print(i)
    return a_list

b_list = series_1(a_list)
print(b_list)

# Series 2
def series_2(b_list):
    b_list.pop()
    print(b_list)
    remove_fruit = input("Enter an item to be removed: ")
    b_list.remove(remove_fruit)
    print(b_list)

series_2(b_list)

# Series 3 
def series_3(a_list):
    answers = []
    b_list = []
    count = 0
    print("Enter 'q' to quit at any time.")
    print("*" * 30)
    while count <= len(a_list) - 1 and answers != "q":
        answers.append(input("Do you like " + a_list[count].lower() + "? "))
        if answers[count] == "no":
            count+=1
        elif answers[count] == "yes":
            b_list.append(a_list[count])
            count+=1
        elif answers[count] == "q":
            break
        else:
            print("Invalid response starting over.")
            return series_3(a_list)
    return b_list

print(series_3(a_list))

# Series 4
def series_4(a_list):
    b_list = []
    for fruit in a_list:
        b_list.append(fruit[::-1])
    a_list.pop()
    print(a_list)
    print(b_list)
    return b_list

series_4(a_list)
