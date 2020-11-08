# ----- SERIES 1 -----
print('SERIES #1')
OGList = ["Apples", "Pears", "Oranges", "Peaches"]
ls = OGList.copy()
print(ls)
# Add fruit to the end
ls.append(input("Please add another fruit: "))
print(ls)
# Display fruit at index input
seq = int(input("Please provide a number for the index: "))-1
print(f'{seq+1}: {ls[seq]}')
# Add a fruit to the beginning
ls = [input("Please add another fruit: ")] + ls
print(ls)
# Add a fruit to the beginning
ls.insert(0, input("Please add another fruit: "))
print(ls)
# Print out the "P" fruits
for ele in ls:
    if ele[0] == "P":
        print(ele)

# ----- SERIES 2 -----
print('SERIES #2')
print(OGList)
# Remove last item
ls = OGList[:-1]
print(ls)
check = True
# Multiply list until a match is deleted
while check:
    search = input("Which fruit would you like to delete? ")
    ls = ls*2
    for ele in ls:
        if ele == search:
            ls.remove(search)
            check = False
print(ls)

# ----- SERIES 3 -----
print('SERIES #3')

s3ls = []
# Determine which elements to keep
for ele in OGList:
    choice = input(f"Do you like {ele}? ").lower()
    while choice != "yes" and choice != "no":
        choice = input("Please respond with yes or no. ")
    if choice == "yes":
        s3ls = s3ls + [ele]
        continue
    if choice == "no":
        continue
print(s3ls)

# ----- SERIES 4 -----
ls = []
# Reverse the letters
for ele in OGList:
    ele4 = ""
    for i in range(len(ele), 0, -1):
        ele4 = ele4 + ele[i-1]
    ls.append(ele4)
# Remove the last fruit from the original
ls4 = OGList[:-1]
print(ls4)
print(ls)
