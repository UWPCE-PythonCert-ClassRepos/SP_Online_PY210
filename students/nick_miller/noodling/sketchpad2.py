donor_db = [
            ("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]

names = []

for i in range(0, (len(donor_db))):
    entry = (donor_db[i])
    name = entry[0]
    names.append(name.lower())

userindex = input(str("enter a name: "))

userindex = userindex.lower()

print(userindex)

if userindex in names:
    pass
else:
    print("that's not in the list")
    exit()

finditem = names.index(userindex)

donor_db_new = list(donor_db)

listtoaddto = donor_db_new[finditem]

itemtoadd = 300.00

itemtoadd = float(f"{itemtoadd:.2f}")

listtoaddto = listtoaddto[1]

listtoaddto.append(itemtoadd)

donor_db_new = tuple(donor_db_new)

# print(donor_db_new)
print(donor_db)
