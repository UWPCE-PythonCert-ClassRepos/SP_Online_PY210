#!/usr/bin/env python3

def series_one(): 
    """
    function uses a list of fruits in a basket
    prompts user for a fruit to add to basket, 
    displays fruit basket, and finally, searches 
    for fruits that start with 'P'
    """
    print()
    print("[+] In series_one function..")

    fruit_basket = ['Apples', 'Pears', 'Oranges', 'Peaches'] 

    print("The fruit basket has the following fruits", fruit_basket)

    fruit = input("Give me a fruit name to add to the fruit basket : ")
    if fruit not in fruit_basket:
        fruit_basket.append(fruit)
    print("The fruit basket now has the following fruits", fruit_basket)

    number = input("Enter a fruit number between " + str(1) + ".." + str(len(fruit_basket)) + " : ")
    number = int(number)
    if number < 1 or number > len(fruit_basket): 
        print("Number has to be in the valid range of " + str(1) + ".." + str(len(fruit_basket)))
    else:
        print("The number you entered is: " + str(number))
        print("The corresponding fruit name to the number you entered is: "  + fruit_basket[number - 1]) 

    print("[+] Adding Dragon Fruit to fruit basket...")
    if 'Dragon Fruit' not in fruit_basket:
        fruit_basket = ['Dragon Fruit', ] + fruit_basket
    else: 
        print("[-] Fruit already exists! Skipping add!")
    print("The fruit basket, now has the following fruits: ", fruit_basket)

    print("[+] Adding Kiwi fruit..")
    if 'Kiwi' not in fruit_basket:
        fruit_basket.insert(0, 'Kiwi')
    else: 
        print("[-] Fruit already exists! Skipping add!")
    print("The fruit basket, now has the following fruits: ", fruit_basket)

    for fruit in fruit_basket:
        if fruit.capitalize().startswith('P'): 
            print("[+] Fruits that start with P are : ", fruit)

    print()

    return fruit_basket

def series_two(fruit_basket): 
    """
    function removes last item in fruit basket, doubles the contents of fruit basket
    , then asks a user for fruit to remove, and remove all occurences of the fruit

    :param: fruit_basket: list of fruits 
    """
    print()
    print("[+] In series_two function..")

    print("Contents for fruit basket : ", fruit_basket)
    print("[+] Removing last fruit from fruit basket..")
    del fruit_basket[-1]
    print("[+] Contents of fruit basket after delete : ", fruit_basket) 
    
    double_fruit_basket = fruit_basket + fruit_basket
    print("[+] Contents of double fruit basket : ", double_fruit_basket) 

    fruit = input("Which fruit would you like to remove from the fruit basket ? : ")
    while fruit in double_fruit_basket:
        double_fruit_basket.remove(fruit.capitalize()) 

    print("[+] Contents of double fruit basket after delete : ", double_fruit_basket) 

def series_three(fruit_basket): 
    """
    Fruit, converts fruit_baskets contents into lower case ,for each fruit, 
    ask user, yes/no for like or dislike for any "no" responses, delete fruit 
    from basket and display end result to the user
    """
    print()
    print("[+] In series_three function..")
    response_yes = "yes"
    response_no  = "no"

    fruit_basket_lowercase = []
    for fruit in fruit_basket: 
        fruit_basket_lowercase.append(fruit.lower())

    for fruit in fruit_basket: 
        response = input("Do you like " +  fruit.lower() +  " (Yes/No) : ")
        response = response.lower()
        while (response != response_yes) and (response != response_no): 
            response = input("Do you like " + fruit.lower() + " (Yes/No) : ")
            response = response.lower()
        # A response of no, means user dislikes fruit. Delete fruit from fruit basket. 
        if response == response_no: 
            fruit_basket_lowercase.remove(fruit.lower())

    print("[+] Heres is the list of fruits you like, in the fruit basket : ", fruit_basket_lowercase)


def series_four(fruit_basket): 
    """
    Function, makes a copy of the orignal list, reverses each item in the copy 
    list and removes item from original list and finally display both lists

    :param: fruit_basket: Original fruit basket to copy from. 
    """
    print()
    print("[+] In series_four function..")
    fruit_basket_copy = fruit_basket[:] 

    index = 0 
    while (index < (len(fruit_basket_copy))): 
        fruit_basket_copy[index] = fruit_basket_copy[index][::-1]
        index = index + 1
    
    print("[+] Contents of fruit basket copy : ", fruit_basket_copy) 

    print("[+] Deleting last item of original fruit basket..")
    del fruit_basket[-1]

    print("[+] Contents of original fruit basket : ", fruit_basket)

if __name__ == '__main__':
    fruit_basket = series_one()
    series_two(fruit_basket)
    series_three(fruit_basket)
    ##fruit_basket = ['Dragon Fruit', 'Apples', 'Pears', 'Oranges', 'Peaches', 'Kiwi']
    series_four(fruit_basket)