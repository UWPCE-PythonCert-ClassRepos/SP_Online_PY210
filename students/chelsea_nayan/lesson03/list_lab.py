# chelsea_nayan, UWPCE, Python 210
# Lesson 03: List Lab Exercise

# Series 1 ----------------------------------
ls = ["Apples", "Pears", "Oranges", "Peaches"]
print(ls)
ls.append(input("Please add another fruit for the list! > "))
print(ls)
num = int(input("Give me a number up to %i, boyo! > "%(len(ls))))
print("You gave me the number %i and the corresponding fruit from the list are %s!"%(num, ls[num-1]))
print(["Blueberries"] + ls) # Adding to the list using list concatenation
ls.insert(0, "Lemons") # Adding to the list using insert
print(ls)
for item in ls: # Prints out the items that start with a "P"
    if "P" in item[0]:
        print(item)
ls2, ls3, ls4 = ls, ls, ls # For ease of testing

# Series 2 -----------------------------------
#ls2 = ["Blueberries", "Apples", "Pears", "Oranges", "Peaches", "Lemons"] <-- Used for testing
print(ls2)
ls2.pop()
print(ls2)
fruit = input("Give me a fruit to delete from the list, boyo! > ")
ls2 = ls2*2 # Includes the bonus challenge!
while fruit not in ls2:
     fruit = input("Give me a fruit from THE LIST, boyo! > ")
for item in ls2:
    if fruit == item:
        ls2.remove(item)
print(ls2)

# Series 3 -----------------------------------
#ls3 = ["Blueberries", "Apples", "Pears", "Oranges", "Peaches", "Lemons"] <-- Used for testing
good_fruits = [] # Modifying the list within the for loop got complicated, so adding the 'liked' fruits to a new list was an easier solution.
for item in ls3:
    like = input("Do you like {}? > ".format(item.lower())).lower() # Makes sure the fruit in the list and user response is turned lowercase
    while like != "yes" and like != "no":
        like = input("Please say 'yes' or 'no' > ").lower()
    if like == "yes":
        good_fruits.append(item) # Adds the ;liked' item to the new list
print(good_fruits)

# Series 4 ---------------------------------------
#ls4 = ["Blueberries", "Apples", "Pears", "Oranges", "Peaches", "Lemons"] <-- Used for testing
reverse_fruit = [] # Created a new list to add in the reverse fruit names
for item in ls4:
    item = item[::-1]
    reverse_fruit.append(item)
ls4.pop() # Just popped off the end of the list
print(ls4, reverse_fruit)
