# ---------------------------------------------------------------------------- #
# Title: list_lab
# Description: Four series of codes for modifying lists
#
# <05/22/2020>, Created Script
# <06/12/2020>, Revised script to incorporate suggestions
# ---------------------------------------------------------------------------- #

# series1:
'''
Step 1 Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
Step 2 Display the list (plain old print()
Step 3 Ask the user for another fruit and add it to the end of the list and display list
Step 4 Ask the user for a number and display the number back to the user with
        the fruit corresponding to that number (on a 1-is-first basis)
Step 5 Add another fruit to the beginning of the list using “+” and display the list
Step 6 Add another fruit to the beginning of the list using insert() and display the list
Step 7 Display all the fruits in the list that begin with the letter “P”, using a for loop
'''

def print_list():
    print("The current list is: ", fruit)

print()
# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print_list() # Display the list using print_list function
# Ask the user for another fruit and add it to the end of the list and display list
fruit_response = input("Add another fruit to the 'end' of the list: ")
print("You typed '{}'!".format(fruit_response))
fruit.append(fruit_response.title())
print_list()
print()
# Ask the user for a number and display the number back to the user with
# the fruit corresponding to that number (on a 1-is-first basis)
number_response = input("Pick a number in the list (1 - 5): ")
print("You picked '{}'!".format(number_response))
while True:
    if (number_response == "1"):
        print("Number 1 in the list = ", '"', fruit[0], '"')
        break
    elif (number_response == "2"):
        print("Number 2 in the list = ", '"', fruit[1], '"')
        break
    elif (number_response == "3"):
        print("Number 3 in the list = ", '"', fruit[2], '"')
        break
    elif (number_response == "4"):
        print("Number 4 in the list = ", '"', fruit[3], '"')
        break
    elif (number_response == "5"):
        print("Number 5 in the list = ", '"', fruit[4], '"')
        break
    else:
        print("Error! you didn't pick a number between 1 and 5!")
        break
print()
# Add another fruit to the beginning of the list using “+” and display the list
fruit_response = input("Add another fruit to the 'beginning' of the list: ")
print("You typed '{}'!".format(fruit_response))
fruit_response_lst = [fruit_response.title()]
fruit = fruit_response_lst + fruit
print_list()
print()
# Add another fruit to the beginning of the list using insert() and display the list
fruit_response = input("Add another fruit to the 'beginning' of the list: ")
print("You typed '{}'!".format(fruit_response))
# Display the list with insert.
fruit.insert(0, fruit_response.title())
print_list()
print()
# Display all the fruits that begin with “P”, using a for loop.
print('Now here are all the fruits in the list that start with the letter "P!"')
p_fruit = []
for p in fruit:
    if p.startswith('P') == True:
        p_fruit.append(p)
print(p_fruit)


def series2(fruit):
    '''
    Step 1 Display the list from series 1
    Step 2 Remove the last fruit from the list
    Step 3 Display the list
    Step 4 Ask the user for a fruit to delete, find it and delete it
    Step 5 (Bonus part1): Multiply the list times two. - completed
    '''
    # make a copy of series 1 fruit list (not bound to each other)
    series2_fruit = fruit[:]

    def print_list():
        print("The current list is: ", series2_fruit)

    print()
    input("Press 'enter' to start 'Series 2'")
    print_list()
    print("Someone ate the last fruit in the list  ",'"', series2_fruit[-1],'"'"\n")
    # use .pop to remove last value in list
    series2_fruit.pop()
    print_list()
    remove_fruit = input("Enter a fruit you would like to eat and remove from the list: ")
    series2_fruit.remove(remove_fruit.title())
    print_list()
    double_it = series2_fruit + series2_fruit
    series2_fruit = double_it
    print()
    print("You went to the store and doubled your list:")
    print_list()

def series3(fruit):
    '''
    Step 1a Display list from series1
    Step 1 Ask the user for input displaying a line like “Do you like apples?”
           for each fruit in the list (making the fruit all lowercase)
    Step 2 For each “no”, delete that fruit from the list
    Step 3 For any answer that is not “yes” or “no”, prompt the user to answer
           with one of those two values (a while loop is good here)
    Step 4 Display the list
    '''
    # make a copy of series 1 fruit list (not bound to each other)
    series3_fruit = fruit[:]

    def print_list():
        print("The current list is: ", series3_fruit)

    print()
    input("Press 'enter' to start 'Series 3'")
    print()
    print("For each fruit in the list Answer if you like it with a 'y' for 'Yes' or 'n' for 'No'")
    print("All fruits that are 'No' will be removed from the list \n")
    print_list()

    while True:
        # revision made here
        # used reverse here, if not all removes will skip the next in the list since the sequence has shifted
        # another option would be to append all the "y" to a new list
        for fruit in reversed(series3_fruit):
            choice = input("Do you like this fruit?..." + "'"+ fruit.lower() + "'" + ",  Enter ('y') or ('n'): ")
            if (choice.lower() == 'y'):
                print(fruit.lower() + " *Saved On List*")
            elif (choice.lower() == 'n'):
                series3_fruit.remove(fruit)
                print(fruit.lower() + " *Removed From List*")
            else:
                print("Please Type ('y') or ('n') only")
        break
    print_list()


def series4(fruit):
    '''
    Step 1a Display list from series1
    Step 1 Make a new list with the contents of the original, but with all the letters in each item reversed
    Step 2 Delete the last item of the original list. Display the original list and the copy
    '''
    # make a copy of series 1 fruit list (not bound to each other)
    series4_fruit_original = fruit[:]
    series4_fruit_poplast = fruit[:]

    def print_list():
        print("The current list is: ", series4_fruit_original)

    print()
    input("Press 'enter' to start 'Series 4'")
    print()
    print_list()
    print()
    print("The new list will now display each fruit's letter in reversed order:")
    # reverse letter order for each fruit
    reversed_fruit = [rev_fruit[::-1] for rev_fruit in series4_fruit_original]
    print(reversed_fruit)
    print()
    print("Here is the original list with the last fruit removed:...*Removed*-" + series4_fruit_poplast[-1])
    # use .pop to remove last value in list
    series4_fruit_poplast.pop()
    print(series4_fruit_poplast)
    print()
    print("Here is the original full list:")
    print(series4_fruit_original)


# run the script functions
series2(fruit)
series3(fruit)
series4(fruit)



