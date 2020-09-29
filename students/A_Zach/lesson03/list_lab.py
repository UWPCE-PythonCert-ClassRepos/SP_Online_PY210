#Series 1

print("Series 1:")
#Create a list of fruits and display
Fruit_one = ["Apples", "Pears", "Oranges", "Peaches"]
print(Fruit_one)

#Request a new fruit
response_1 = input("Please add another fruit to the list > ")

#Add the new fruit to the list and display
Fruit_one.append(response_1)
print(Fruit_one)

#Store the length of the list. Use this to ask for any number between 1 and the length of the list
Length = len(Fruit_one) + 1
response_2 = input("Give me a number between 1 and " + str(Length-1) + " and I'll give you a fruit > ")

#Display the number given and the corresponding fruit in the list
print(response_2, ", ", Fruit_one[int(response_2) - 1])

#Add a new fruit to the beginning of the list with + and display
Fruit_one = ["Papaya"] + Fruit_one
print(Fruit_one)

#Add a new fruit to the beginning of the list with insert function and display
Fruit_one.insert(0,"Banana")
print(Fruit_one)

#Display fruits beginning with "P"
for n in Fruit_one:
    if n[0] is "P":
        print(n)
        
#Series 2

#display series name
print("Series 2:")


#print the list from series 1
Fruit_two = ["Apples", "Pears", "Oranges", "Peaches"]
print(Fruit_two)

#Remove the last entry and display
del Fruit_two[-1]
print(Fruit_two)

#Ask for a fruit to delete
Del_frt = input("Give me a fruit to delete from the list diplayed above >")

#Delete the fruit
Fruit_two.remove(Del_frt)
print(Fruit_two)

#Try it again with a list with multiple of the same entry
Double_Fruit_two = ["Apples", "Pears", "Oranges", "Peaches"]*2
print(Double_Fruit_two)

#Ask for a fruit to delete
Del_frt = input("Give me a fruit to delete from the list diplayed above >")
while Del_frt not in Double_Fruit_two:
    print(Del_frt, " is not in the list of fruits.")
    Del_frt = input("Give me a fruit to delete from the list diplayed above >")
    
#Delete all instances of provided fruit
while Del_frt in Double_Fruit_two:
    Double_Fruit_two.remove(Del_frt)

print(Double_Fruit_two)

#Series 3
print("Series 3:")

#Recreate the original list
Fruit_Three = ["Apples", "Pears", "Oranges", "Peaches"]

#Ask the user if they like each fruit on the list
for n in Fruit_Three:
    Response = input("Do you like " + n + "?>")
    #make sure the answer is yes or no
    while Response not in ["yes", "no"]:
        Response = input('Please respond with "yes" or "no">')
    #Remove all fruits the user doesn't like
    if Response is "no":
        Fruit_Three.remove(n)

print(Fruit_Three)

#Series 4
print("Series 4:")
#Recreate the original list
Fruit_Four = ["Apples", "Pears", "Oranges", "Peaches"]

#Create a new list 
Reversed_Fruit_Four = []
#Reverse the letters in each list entry
for n in Fruit_Four:
    #create a new list with reversed letters from the original list
    Reversed_Fruit_Four.append(n[::-1])

#Remove last entry in original list
del Fruit_Four[-1]

print(Fruit_Four)
print(Reversed_Fruit_Four)
