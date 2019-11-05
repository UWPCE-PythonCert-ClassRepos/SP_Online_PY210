#!/usr/bin/env python3

"""
lsit_lab.py
By David Baylor on 10/17/19
uses python 3

Demonstrates basic list manipulation.
"""

def series1(fruit):
    """series 1"""
    print("Series 1")
    print(fruit)
    fruit.append(input("Name another fruit: "))
    print(fruit)
    step = int(input("Pick a number between 1 and {}: ".format(len(fruit))))
    print(step, ": ", fruit[step - 1])
    fruit = [input("name another fruit: "),] + fruit
    print(fruit)
    fruit.insert(0, input("Name another fruit: "))
    print(fruit)
    for i in range(len(fruit)):
        if fruit[i][0] == "P":
            print(fruit[i])


def series2(fruit):
    """series 2"""
    print("Series 2")
    print(fruit)
    del(fruit[-1])
    print(fruit)
    remove_fruit = input("Pick a fruit to remove: ")
    for i, item in enumerate(fruit):
        if item == remove_fruit:
            print(i, item)
            del(fruit[i])
    print(fruit)

def series3(fruit):
    """series 3"""
    print("Series 3")
    del_list = []
    for item in fruit:
        while True:
            answer = input("Do you like {}? ".format(item.lower()))
            if answer.lower() == "yes":
                break
            elif answer.lower() == "no":
                del_list.append(item)
                break
    for i, item in enumerate(fruit):
        if item in del_list:
            del(fruit[i])
    print(fruit)

def series4(fruit):
    """series 4"""
    print("Series 4")
    new_fruit = fruit[:]
    for i, item in enumerate(new_fruit):
        new_fruit[i] = item[::-1]
    del(fruit[-1])
    print(fruit)    
    print(new_fruit)    


fruit = ["Apples","Pears","Oranges","Peaches"]
series1(fruit)
fruit = ["Apples","Pears","Oranges","Peaches"]
series2(fruit)
fruit = ["Apples","Pears","Oranges","Peaches"]
series3(fruit)
fruit = ["Apples","Pears","Oranges","Peaches"]
series4(fruit)



