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

    # Get copies of the fruit list so that we can manipulate them
    series2_fruits = fruits[:]
    series3_fruits = fruits[:]
    series4_fruits = fruits[:]
    

    # Series 2 instructions
    print(series2_fruits)
    del series2_fruits[-1:]
    print(series2_fruits)
    series2_fruits = 2 * series2_fruits
    fruit_length = len(series2_fruits)

    while len(series2_fruits) == fruit_length:
        print(series2_fruits)
        delete_fruit = input("Which fruit would you like to be removed?: ")
        for fruit in series2_fruits:
            if fruit == delete_fruit:
                series2_fruits.remove(fruit)

        if len(series2_fruits) == fruit_length:
            print("That fruit is not in the list. Try again.")
        else:
            print(series2_fruits)

if __name__=='__main__':
    main()


