#!/usr/bin/env python3

def series_1():
    """
    Return list of fruit that has been added to by prompt
    """

    fruit_list = ['Apples','Pears','Oranges','Peaches']
    print(fruit_list)

    fruit_to_add = input("What additional fruit sbould be added?")
    fruit_list.append(fruit_to_add)
    print(fruit_list)

    fruit_number = input("Request fruit to be shown based on position:")
    print("You have requested to see fruit {}: {}".format(int(fruit_number), fruit_list[int(fruit_number)-1]))

    #Add another fruit to the beginning of the list using plus and display the list.
    additional_fruit_to_add = ['Melon']
    fruit_list = additional_fruit_to_add + fruit_list
    print(fruit_list)

    #Add another fruit to the beginning of the list using insert() and display the list.
    additional_fruit_to_add = 'Strawberries'
    fruit_list.insert(0,additional_fruit_to_add)
    print(fruit_list)

    fruit_with_p = []
    for fruit in  fruit_list:
        if 'p' in fruit.lower():
            fruit_with_p.append(fruit)
    print('Fruits with Ps are:')
    print(fruit_with_p)

    return fruit_list

def series_2(fruit_list):
    """
    Return list of fruit that has elements deleted by prompt
    :param fruit_list: Requested fruit list to be trimmed
    """
    trimmed_fruit_list = fruit_list[:-1]
    print("Here is the fruit list without the last item:")
    print(trimmed_fruit_list)

    fruit_to_remove = ''
    while fruit_to_remove not in trimmed_fruit_list:
        fruit_to_remove = input("What additional fruit sbould be removed?")
        if fruit_to_remove in trimmed_fruit_list:
            trimmed_fruit_list.remove(fruit_to_remove)
            print(trimmed_fruit_list)
            break
        else:
            print('Fruit requested was not in the list.')

    return trimmed_fruit_list

def series_3(fruit_list):
    """
    Return list of fruit that only includes fruit that users like
    :param fruit_list: Requested fruit list to sort
    """
    question = "Do you like {}?"
    liked_fruit = fruit_list[:]

    for fruit in fruit_list:
        fruit_preference = input(question.format(fruit.lower()))
        while fruit_preference.lower() not in ['yes','no']:
            print('Please type "yes" or "no".')
            fruit_preference = input(question.format(fruit.lower()))
        if fruit_preference == 'no':
            liked_fruit.remove(fruit)

    return liked_fruit

def series_4(seq):
    """
    Return list with elements sequences reversed and remove last element
    :param seq: Requested sequemnce to reverse and trim
    """
    reversed_seq = seq[:]
    for i, item in enumerate(seq):
        reversed_seq[i] = seq[i][::-1]

    del seq[-1]
    del reversed_seq[-1]

    print(seq)
    print(reversed_seq)


    return reversed_seq[:-1]
