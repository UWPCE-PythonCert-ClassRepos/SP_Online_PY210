#!/usr/bin/env python3

def series_one(l):
    print (l)
    fruit = input("Please type in a fruit: ")
    l.append(fruit)
    print (l)
    num = int(input("\nPlease enter in a fruit number (1-5): "))
    while num > 5 or num < 1:
        num = int(input("Please enter in a fruit number (1-5): "))
    print (num, l[num -1])
    l = ["Mellon"] + l
    print (l)
    l.insert(0, "Pineapple")
    print (l)
    print ("\nFruits that start with 'P'")
    for i in l:
        if i[0] == "P":
            print (i)
    return l

def series_two(l):
    print (l, "\n")
    l.pop()
    print (l, "\n")
    elim_element = input("Please type in a fruit to delete: ")
    l = l *2
    while not elim_element in l:
        elim_element = input("That fruit is not available to delete. Please type in a fruit to delete: ")
    while elim_element in l:
        l.remove(elim_element)  
    print (l)

l = ["Apples", "Pears", "Oranges", "Peaches"]
l_2 = series_one(l)
series_two(l_2)