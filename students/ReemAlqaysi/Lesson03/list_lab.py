#!/usr/bin/env python3

def series1():
    mylist =  ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(mylist)
    #Ask the user for another fruit and add it to the end of the list.
    response = input("add another fruit please: ")
    mylist.append(response)
    print(mylist)
    response2 = input("Provide a number between 1 and {:d}: ".format(len(mylist)))
    print(response2 + " is the index number for : " + mylist[int(response2)-1])
    #Add another fruit to the beginning of the list using “+” and display the list.
    mylist =  mylist +['Banana']
    print(mylist)
    #Add another fruit to the beginning of the list using insert() and display the list.
    mylist.insert(0,'Mango')
    #Display all the fruits that begin with “P”, using a for loop.
    print("Display all the fruits that begin with “P”, using a for loop.")
    for name in mylist:
        if name[0].upper() == "P":
            print(name)
        else:
            continue
    return mylist

def series2(mylist):
    print(mylist)
    #Remove the last fruit from the list.
    mylist.pop()
    print("Remove the last fruit from the list.")
    print(mylist)
    #Ask the user for a fruit to delete, find it and delete it.
    response = input("please print a fruit to delete: ")
    for fruit in mylist:
        if response == fruit:
            mylist.remove(response)
            break
    else:
        print ('this fruit not exist in the list')
        
    print(mylist)

def series3(mylist):
    for fruit in mylist[:]:
        response = input("Do you like " + fruit.lower() + "?\n")
        #For each “no”, delete that fruit from the list.
        if response == "no":
            mylist.remove(fruit)
        elif response == "yes":
            continue
        else:
            response = input("Please answer yes or no. Do you like " + fruit.lower() + "?\n")
    print(mylist)


def series4(mylist):
    newlist = []
    #Make a new list with the contents of the original, but with all the letters in each item reversed.
    for fruit in mylist:
        newlist.append(fruit[::-1])
    print("Delete the last item of the original list.")
    mylist.pop()
    print(mylist)
    print("all the letters in each item reversed.")
    print(newlist)



if __name__ == '__main__':
    series1_list = series1()
    series2(series1_list)
    series3(series1_list)
    series4(series1_list)