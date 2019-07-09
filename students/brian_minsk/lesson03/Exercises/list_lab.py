# Author: Brian Minsk

def main():
    """ Call the other functions which do the actual work.
    """
    list_fruit = ["Apples", "Pears", "Oranges", "Peaches"]
    list_fruit2 = series1(list_fruit)
    series2(list_fruit2)
    series3(list_fruit2)
    series4(list_fruit2)

def series1(list_fruit):
    """ This is a straight-forward implementation of Series 1 section of the List Lab script described at
    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html

    1. Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”. (This was done in main())
    2. Display the list (plain old print() is fine…).
    3. Ask the user for another fruit and add it to the end of the list.
    4. Display the list.
    5. Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
    6. Add another fruit to the beginning of the list using “+” and display the list.
    7. Add another fruit to the beginning of the list using insert() and display the list.
    8. Display all the fruits that begin with “P”, using a for loop.

    Keyword arguments:
    list_fruit -- list of strings
    """
    #2
    print(list_fruit)
    #3
    new_fruit = input("Please type a new fruit name: ")
    list_fruit.append(new_fruit)
    #4
    print(list_fruit)
    #5
    number = 0
    while number < 1 or number > len(list_fruit):
        str_number = input("Please type a number from 1 to {:d}: ".format(len(list_fruit)))
        number = int(str_number)
        if number > 0 and number <= len(list_fruit):
            break
    print(str(number) + " " + list_fruit[number - 1])
    #6
    new_fruit = input("Please type another new fruit name: ")
    list_fruit = [new_fruit] + list_fruit
    print(list_fruit)
    #7
    new_fruit = input("Please type yet another new fruit name: ")
    list_fruit.insert(0, new_fruit)
    print(list_fruit)
    #8
    print("Fruits that begin with the letter 'P'")
    for fruit in list_fruit:
        if fruit[0].upper() == "P":
            print(fruit)
    return list_fruit

def series2(list_fruit):
    """ This is a straight-forward implementation of Series 2 section of the List Lab script described at
    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html

    Using the list created in series 1 above:
    1. Display the list.
    2. Remove the last fruit from the list.
    3. Display the list.
    4. Ask the user for a fruit to delete, find it and delete it.
    5. (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

    Keyword arguments:
    list_fruit -- list of strings
    """
    #1
    print(list_fruit)
    #2
    del list_fruit[-1]
    #3
    print (list_fruit)
    #5 (skip 4 and do the bonus)
    double_list_fruit = list_fruit * 2
    fruit_to_delete = ""
    while True: 
        fruit_to_delete = input("Please type a fruit to delete: ")
        if not fruit_to_delete in double_list_fruit:
            continue
        while True:
            if fruit_to_delete in double_list_fruit:
                double_list_fruit.remove(fruit_to_delete)
            else:
                break 
        break
    print(double_list_fruit) 

def series3(list_fruit):
    """ This is a straight-forward implementation of Series 3 section of the List Lab script described at
    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html

    Again, using the list from series 1:
    1. Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    2. For each “no”, delete that fruit from the list.
    3. For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here)
    4. Display the list.

    Keyword arguments:
    list_fruit -- list of strings
    """
    list_fruit_iterable = list_fruit[:] # need to make a copy because items in list_fruit will be deleted and it will mess up the iteration of the for loop
    # 1
    for fruit in list_fruit_iterable:
        likes_the_fruit = input("Do you like {}? ".format(fruit.lower()))
        #3
        while not likes_the_fruit.lower() == "no" and not likes_the_fruit.lower() == "yes":
            likes_the_fruit = input("Please type 'yes' or 'no': ")
        #2
        if likes_the_fruit.lower() == "no":
            while True:
                if fruit in list_fruit:
                    list_fruit.remove(fruit)
                else:
                    break
    # 4
    print(list_fruit)

def series4(list_fruit):
    """ This is a straight-forward implementation of Series 3 section of the List Lab script described at
    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html

    Once more, using the list from series 1:
    1. Make a new list with the contents of the original, but with all the letters in each item reversed.
    2. Delete the last item of the original list. Display the original list and the copy.

    Keyword arguments:
    list_fruit -- list of strings
    """
    # 1
    list_fruit_reversed_letters = []
    for fruit in list_fruit:
        list_fruit_reversed_letters.append(fruit[::-1])
    # 2
    list_fruit.pop()
    print(list_fruit)
    print(list_fruit_reversed_letters)

if __name__ == "__main__":
    main()