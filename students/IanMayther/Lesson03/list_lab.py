#!/usr/bin/env python3



if __name__ == "__main__":
#Series 1
    #First Bullet
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

    #Second Bullet
    print(fruits)

    #Third Bullet
    response = input("Can you add another fruit?")
    fruits.append(response)

    #Fourth Bullet
    print(fruits)

    #Fifth Bullet
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
        if item[:1] == "P" or item[:1] == "p":
            p_fruits.append(item)
    print(f"All the Fruits that begin with P: {p_fruits}")

#Series 2
    #First Bullet
    print(fruits)

    #Second Bullet
    print("Removing Last Item.")
    fruits.pop()
    
    #Third Bullet
    print(f"New List: {fruits}")

    #Fourth Bullet
    fruits2 = fruits[:]
    Not_In_List = False
    while Not_In_List == False:
        response = input(f"What Fruit should we remove? {fruits2}")
        for i in range(len(fruits)):
            if response == fruits[i]:
                fruits2.pop(i)
                Not_In_List = True
        if Not_In_List == False:
                print("Please select an Item in the list.")
    print(f"Series 2 List: {fruits2}")  

#Series 3
    fruits3 = []
    print(f"Series 3 List: {fruits}")
    for i, item in enumerate(fruits[:]):
        definite = False
        while definite == False:
            response = input(f"Do you like {fruits[i].lower()}? Y/N - ")
            if response == "Y":
                definite = True
                fruits3.append(fruits[i])                
            elif response == 'N':
                definite = True
            else:
                print("Please select Y or N") 
                definite = False

    print(fruits3)

#Series 4
    fruits4 = fruits[:]
    for i in range(len(fruits4)):
        seq = fruits4[i]
        fruits4[i] = seq[::-1]

    print(f"Original List: {fruits}")
    print(f"Reversed List: {fruits4}")
