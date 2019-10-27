#!/usr/bin/env python3
def main():    
    
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]

    print(fruits)

    # Get user input for adding more fruit to the list 
    more_fruit = input("Please add another fruit to the list: ")
    fruits.append(more_fruit)
    print(fruits)
    index = int(input("Choose a fruit number based on the order it appears in the list: "))
    print(fruits[index - 1])

    # Add another fruit to the list using the + symbol
    fruits = ["Coconuts"] + fruits
    print(fruits)

    # Add another fruit to the list using the insert method
    fruits.insert(0, "Bananas")
    print(fruits)

    #Print all fruits in the list that start with 'P'
    for item in fruits:
        if item[0] == "P":
            print(item)

    # Get copies of the fruit list so that we can manipulate them later on
    series2_fruits = fruits[:]
    series3_fruits = fruits[:]
    series4_fruits = fruits[:]
    

    # Series 2 instructions
    print(series2_fruits)
    del series2_fruits[-1]
    print(series2_fruits)
    series2_fruits = 2 * series2_fruits
    print(series2_fruits)
    
    delete_fruit = input("Which fruit would you like to be removed?: ")
    while delete_fruit not in series2_fruits:
        delete_fruit = input("That fruit is not in the list. Try again: ") 

    index = len(series2_fruits) - 1
    while index >= 0:
        if delete_fruit == series2_fruits[index]:
            del series2_fruits[index]
        index -= 1        
    print(series2_fruits)

    """ Ask the user for input displaying a line like “Do you like apples?” 
        for each fruit in the list (making the fruit all lowercase).
        For each “no”, delete that fruit from the list.
        For any answer that is not “yes” or “no”, prompt the user to answer 
        with one of those two values (a while loop is good here)
        Display the list."""

    #Series 3 
    temp = []
    for element in series3_fruits:
        fruit_prefs = input(f"Do you like {element.lower()}? ")
        while fruit_prefs != "no" and fruit_prefs != "yes":
            fruit_prefs = input(f"Use only 'yes' or 'no'. Please try again: ")
        if fruit_prefs == "yes":
            temp.append(element)
    series3_fruits = temp
    print(series3_fruits)

    #Make a new list with the contents of the original, but with all the letters in each item reversed.
    #Delete the last item of the original list. Display the original list and the copy.
    fruit_in_reverse = []
    reverse_index = len(series4_fruits) - 1

    while reverse_index >= 0:
        fruit_in_reverse.append(series4_fruits[reverse_index])
        reverse_index -= 1

    del series4_fruits[-1]
    print(series4_fruits)
    print(fruit_in_reverse)

if __name__=='__main__':
    main()