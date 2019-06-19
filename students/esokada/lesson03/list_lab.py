#Series 1
print("Series 1")
mylist = ["Apples", "Pears", "Oranges", "Peaches"]
print(mylist)
response = input("Please enter another fruit:\n")
mylist.append(response)
print(mylist)
response = input("Please enter a number:\n")
print(response + " " + mylist[int(response)-1])
mylist = ["Kumquats"] + mylist
print(mylist)
mylist.insert(0, "Plums")
print(mylist)
for i in mylist:
    if i[0] == "P" or i[0] == "p":
        print(i)

#Series 2

print("Series 2")
print(mylist)
mylist.pop()
print(mylist)
response = input("Tell me a fruit to delete:\n")
mylist.remove(response)
print(mylist)

#Series 3

print("Series 3")
for i in mylist[:]:
    response = input("Do you like " + i.lower() + "?\n")
    while True:
        if response == "no":
            mylist.remove(i)
            break
        elif response == "yes":
            break
        else:
            response = input("Please answer yes or no. Do you like " + i.lower() + "?\n")
print(mylist)

#Series 4

print("Series 4")
newlist = []
for i in mylist:
    newlist.append(i[::-1])
mylist.pop()
print(mylist)
print(newlist)