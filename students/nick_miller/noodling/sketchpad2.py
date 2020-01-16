donor_db = [
            ("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]
# this takes the donor db and creates a new list with just the names to check against (puts them in lower case)
names = []
for i in range(0, (len(donor_db))):
    entry = (donor_db[i])
    name = entry[0]
    names.append(name.lower())

# takes user input, puts it in lower case
userindex = input(str("enter a name: "))
userindex = userindex.lower()
# checks if the lower case name is in the list
if userindex in names:
    pass
else:
    print("that's not in the list")
    exit()
# gets the index in the names list of the name
finditem = names.index(userindex)
# makes a new list from the donor db
donor_db_new = list(donor_db)
# finds the list to add to (the list after the name)
listtoaddto = donor_db_new[finditem]
# gets input for a new donation
itemtoadd = float(input("enter a new donation amount: "))
listtoaddto = listtoaddto[1]
listtoaddto.append(itemtoadd)
# donor_db_new = tuple(donor_db_new)
print(donor_db)
