#!/usr/bin/env python3
def series1():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruits)

    # Get user input for adding more fruit to the list 
    more_fruit = input("Please add another fruit to the list: ")
    fruits.append(more_fruit)
    print(fruits)
    index = int(input("Choose a fruit by its number by the order it appears in the list: "))
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


if __name__=='__main__':
    series1()
