#!/usr/bin/env python3


def series1(seq):
    fruit_list = seq[:]
    print(fruit_list)
    response = input("Please provide another fruit to add: ")
    fruit_list.append(response)
    print(fruit_list)
    number_response = input("Provide a number between 1 and {:d}: ".format(len(fruit_list)))
    print(fruit_list[int(number_response) - 1])
    fruit_list = ["Kiwis"] + fruit_list
    print(fruit_list)
    fruit_list.insert(0, "Mangoes")
    print(fruit_list)
    p_list = []
    for fruit in fruit_list:
        test = fruit[0].upper()
        if fruit[0].upper() == "P":
            p_list.append(fruit)
    print(p_list)


if __name__ == '__main__':
    original_fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    series1(original_fruit_list)
