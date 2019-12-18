#!/usr/bin/env python3


def main():
    # SERIES ONE
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)

    newfruit = input("Fruit: ")
    fruits.append(newfruit)
    print(fruits)

    idxinput = input("Number: ")
    # make sure the input is actually a valid number
    try:
        idx = int(idxinput)
    except ValueError:
        print("Input must be a number!")
        exit(1)
    if idx < 1 or idx > len(fruits):
        print("Bad number!")
        exit(1)
    print(fruits[idx-1])

    fruits = ['Bananas'] + fruits
    print(fruits)

    newfruit2 = input("Fruit: ")
    fruits.insert(0, newfruit2)
    print(fruits)

    for fruit in fruits:
        if fruit[0].lower() == "p":
            print(fruit)

    # SERIES TWO
    print(fruits)
    fruits.pop()
    print(fruits)

    rmfruit = input("Fruit to Remove: ")
    for fruit in fruits:
        if fruit.lower() == rmfruit.lower():
            fruits.remove(fruit)
    print(fruits)

    # SERIES THREE
    # fruits.remove(fruit) inside a for loop is a bad idea, it results in
    # values being skipped in the list. using a second list works around the
    # problem, but definitely isn't ideal
    fruits2 = []
    for fruit in fruits:
        while True:
            userask = input("Do you like {}? (Y/n) ".format(fruit.lower()))
            if userask.lower() == "n":
                break
            elif userask == "y" or userask == "":
                fruits2.append(fruit)
                break
            else:
                print("Invalid input, must be 'y' or 'n'.")
    fruits = fruits2
    print(fruits)

    # SERIES FOUR
    stiurf = []
    for fruit in fruits:
        stiurf.append(fruit[::-1])
    fruits.pop()
    print(fruits)
    print(stiurf)


if __name__ == "__main__":
    main()
