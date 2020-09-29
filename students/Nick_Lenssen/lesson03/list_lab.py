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
    print ("\n",l, "\n")
    l = l[:-1]
    print (l, "\n")
    elim_element = input("Please type in a fruit to delete: ")
    l = l *2
    while not elim_element in l:
        elim_element = input("That fruit is not available to delete. Please type in a fruit to delete: ")
    while elim_element in l:
        l.remove(elim_element)  
    print (l, '\n')

def series_three(l):
    l_copy = l[:]
    for i in l_copy:
        yay_nay = input("Do you like {}: ".format(i.lower()))
        while yay_nay.lower() != "yes" and yay_nay.lower() != "no":
            yay_nay = input("Do you like {}: ".format(i.lower()))
        if yay_nay.lower() == "no":
            l.remove(i)
        else:
            continue
    print (l, "\n")

def series_four(l):
    l_reverse = []
    for i in l:
        l_reverse.append(i[::-1])
    l.pop()
    print (l_reverse)
    print (l)

l = ["Apples", "Pears", "Oranges", "Peaches"]
l_2 = series_one(l)
l_3 = l_2[:] #not sure If i need to make copies here. Lists are mutable so each function following sereis 1 will be manipulating it
l_4 = l_2[:]
series_two(l_2)
series_three(l_3)
series_four(l_4)



