#Mark McDuffie
#Lesson3
#list lab

def seq1(list):
#let user add fruit to the list
    fruit = input("What fruit would you like to add? ")
    list.append(fruit)
    print(list)
#index fruit list and let user select a fruit
    number = input("What number of fruit would you like to select? ")
    fruitIndex = list[int(number) - 1]
    print(number + " " + fruitIndex)
#add fruit at beginning
    newFruit = ["Blackberry"]
    list = newFruit + list
    print(list)
#insert fruit at beginning
    list.insert(0, "Pineapple")
    print(list)
#iterate through list selecting all elements beginning with P
    newList = []
    x = len(list)
    for i in range(x):
        if(list[i].startswith("P")):
            newList.append(list[i])
    print(newList)


def seq2(list):
#display list
    print(list)
#remove last item from list
    list.remove(list[-1])
    print(list)
#ask user to delete a fruit
    fruit = input("what fruit would you like to delete? ")
    if fruit in list:
        list.remove(fruit)
    print(list)

#Asks user whether they like a fruit or not,
#prints the list only containing the fruit that the user likes
#repromts the user if the answer isnt yes/no
def seq3(list):
    newlist = []
    x = len(list)
    for i in range(x):
        fruit = list[i].lower()
        answer = input("Do you like " + fruit + "? ")
        if answer == 'yes':
            newlist.append(list[i])
        while(answer != "yes" and answer != "no"):
            print("Please enter yes/no as an answer.")
            answer = input("Do you like " + fruit + "? ")
    print(newlist)

#Takes list, and prints every element backwards
#while removing the last element and maintaining the original list
def seq4(list):
    newlist = list
    x = len(newlist)
    for i in range(x):
        str = newlist[i]
        y = len(str)
        backwards = str[y::-1]
        newlist[i] = backwards
    newlist.remove(newlist[-1])
    list = ["Apples", "Pears", "Oranges", "Peaches"]
    print(list)
    print(newlist)
#establish list used in all methods
list = ["Apples", "Pears", "Oranges", "Peaches"]
#call entire function
seq1(list)
seq2(list)
seq3(list)
seq4(list)