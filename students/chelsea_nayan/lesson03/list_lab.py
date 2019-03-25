# chelsea_nayan, UWPCE, Python 210
# Lesson 03: List Lab Exercise

# Series 1 ----------------------------------
ls = ["Apples", "Pears", "Oranges", "Peaches"]
print(ls)
ls.append(input("Please add another fruit for the list! > "))
print(ls)
num = int(input("Give me a number up to %i, boyo! > "%(len(ls))))
print("You gave me the number %i and the corresponding fruit from the list are %s!"%(num, ls[num-1]))
print(["Blueberries"] + ls) # Adding to the list using list addition
ls.insert(0, "Lemons") # Adding to the list using insert
print(ls)
for item in ls: # Prints out the items that start with a "P"
    if "P" in item[0]:
        print(item)

# Series 2 -----------------------------------
print(ls)
ls.pop()
print(ls)
fruit = input("Give me a fruit to delete from the list, boyo! > ")
ls = ls*2 # Includes the bonus challenge!
while fruit not in ls:
     fruit = input("Give me a fruit from THE LIST, boyo! > ")
for item in ls:
    if fruit == item:
        ls.remove(item)
print(ls)

# Series 3 -----------------------------------
