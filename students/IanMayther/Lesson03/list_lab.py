#!/usr/bin/env python3



if __name__ == "__main__":
# Series 1
    #First Bullet
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

    #Second Bullet
    print(fruits)

    #Third Bullet
    response = input("Can you add another fruit?")
    fruits.append(response)

    #Fourth Bullet
    print(fruits)

    #Fifit Bullet
    number = input(f"Please provide a number between 1 and {len(fruits)}?")
    if int(number) > len(fruits):
        print(f"Value too large, using {len(fruits)}")
        number = len(fruits)
    print(f"The number you picked, {number}, corresponds with {fruits[int(number)-1]}")

    #Sixth Bullet
    print(fruits)
    response = input("Can you add another fruit?")
    fruits = [response] + fruits
    print(fruits)

    #Seventh Bullet
    response = input("Can you add another fruit?")
    fruits.insert(0, response)
    print(fruits)

    #Eighth Bullet
    p_fruits = []
    for item in fruits:
        if item[:1] == "P":
            p_fruits.append(item)
    print(p_fruits)