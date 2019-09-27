#!/usr/bin/env python3

# ------------------------------ #
# List Lab Assignment for Python 210
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 8/8/2019, Created and tested script
# ------------------------------ #

# ---------- DATA ---------- #
# -------------------------- #
myList = [] # list to manipulated in processing
sub_List = [] # stores a list of selected items pulled from myList
Series1 = [] # stores final list created in Series 1
response = "" # user input responses

# ---------- PROCESSING ---------- #
# -------------------------------- #

def print_list(seq, message = ""):
    print(message)
    print(seq)
    print()

# ---------- PRESENTATION ---------- #
# ---------------------------------- #

# ----- Series 1 ----- #

response = input("Run Series 1? (Y/N): ")
print()
if response.upper() == "Y":
    myList = ["Apples", "Pears", "Oranges", "Peaches"]
    print_list(myList, "The current list items are:")

    response = input("Name a fruit would you like added to the end of this list: ")
    print()
    myList.append(response)
    print_list(myList, "The current list items are:")

    response = int(input("Which item (number) in the list of fruits would you like to view?: "))
    print()
    interim = str(response), "-", str(myList[response - 1])
    interim = ''.join(interim)
    print_list(interim, "The item you requested is: ")

    response = input("What fruit would you like added to the beginning of the list?: ")
    print()
    myList = [response] + myList
    print_list(myList, "The current list items are:")

    response = input("Name another fruit you would like added to the beginning of the list?: ")
    print()
    myList.insert(0, response)
    print_list(myList, "The current list items are:")

    for i in myList:
        if i[0].upper() == "P":
            sub_List.append(i)
    print_list(sub_List, "Here are all the fruits in the list that start with the letter 'P'")
    sub_List = []

    Series1 = myList[:] # stores final list created in Series 1
else:
    myList = ["Apples", "Pears", "Oranges", "Peaches"]
    Series1 = myList[:]


# ----- Series 2 ----- #

response = input("Run Series 2? (Y/N): ")
print()
if response.upper() == "Y":
    print_list(myList, "The current list items are:")

    myList.pop()
    print_list(myList, "With the last item removed...")

    response= input("Which other fruit would you like to remove?: ")
    for item in myList:
        if item.upper() == response.upper():
            myList.remove(item)
    print_list(myList, "Here is your updated list: ")


# ----- Series 3 ----- #

response = input("Run Series 3? (Y/N: ")
print()
if response.upper() == "Y":
    myList = Series1[:]
    print_list(myList, "The current list items are:")

    for item in myList:
        response = input("Do you like " + item + "? (Y/N)").upper()
        while response != "Y" and response != "N":
            response = input("Please enter Y or N: ").upper()
        if response == "Y":
            sub_List.append(item)

    print_list(sub_List, "Here is a list of what you like!")
    sub_List = []


# ----- Series 4 ----- #

response = input("Run Series 4? (Y/N): ")
if response.upper() == "Y":
    myList = Series1[:]

    print_list(myList[::-1], "REVERSE! REVERSE!")

    origList = myList[:]
    myList.pop()
    print_list(myList, "Copy:")
    print_list(origList, "Original:")
    print_list(myList, "Copy:")
