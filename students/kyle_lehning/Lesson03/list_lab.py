#!/usr/bin/env python3


def series1(seq):
    print("***************SERIES 1***************")
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
        if fruit[0].upper() == "P":
            p_list.append(fruit)
    print(p_list)
    return fruit_list


def series2(seq):
    print("***************SERIES 2***************")
    fruit_list = seq[:]
    print(fruit_list)
    del fruit_list[-1:]
    print(fruit_list)
    removal = input("which fruit would you like to remove: ")
    fruit_list.remove(removal)
    print(fruit_list)


def series3(seq):
    print("***************SERIES 3***************")
    fruit_list = seq[:]
    for fruit in fruit_list[:]:
        removal = input("Do you like {}? (yes/no): ".format(fruit))
        while removal not in ("yes", "no"):
            removal = input("please provide a yes or no answer: ")
        if removal == "no":
            fruit_list.remove(fruit)
    print(fruit_list)


def series4(seq):
    print("***************SERIES 4***************")
    letter_reverse_list = []
    for fruit in seq:
        letter_reverse_list.append(fruit[::-1])
    print(letter_reverse_list)
    copy_list = seq[:]
    del copy_list[-1:]
    print(copy_list)
    print(seq)


if __name__ == '__main__':
    original_fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
    series1_list = series1(original_fruit_list)
    series2(series1_list)
    series3(series1_list)
    series4(series1_list)
