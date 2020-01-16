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

# print(names)

# def report(db=donor_db):
#     print(donor_db)
#     print()
#     key = ["name", "total given", "num gifts", "average gift"]
#     separator = "|"
#
#     print(f"{key[0]:<18}",
#           f"{separator:^3}",
#           f"{key[1]:<18}",
#           f"{separator:^3}",
#           f"{key[2]:>10}",
#           f"{separator:^3}",
#           f"{key[3]:>15}")
#     print("-"*76)
#
#     for i in range(0, (len(donor_db))):
#         entry = (donor_db[i])
#         name = entry[0]
#         # print(name)
#         dons = entry[1]
#         totes = sum(dons)
#         # print(totes)
#         nums = len(dons)
#         # print(nums)
#         aves = totes/nums
#         # print(aves)
#         print(f"{name:<18}",
#           f"{separator:^3}",
#           f"{totes:>18.2f}",
#           f"{separator:^3}",
#           f"{nums:^10}",
#           f"{separator:^3}",
#           f"{aves:>15.2f}")
#
# report()

thanksC = str(input("Enter a name or type 'list': "))
thanksC = thanksC.lower()
if thanksC.strip() == "list":
    for i in range(0, (len(donor_db))):
        entry = (donor_db[i])
        name = entry[0]
        print(name)
elif thanksC.lower() not in names:
    addQ = str(input("That name is not in the list, would you like to add it? (y/n): "))
    addQ = addQ.lower()
    if addQ.strip() == "n":
        pass
    if addQ.strip() == "y":
        print("Adding", thanksC.title(), "to the donor list.")
        addY = float(input("Please enter their donation amount: "))
        print("Adding " + thanksC.title() + "'s donation of $" + f"{addY:.2f}", "to their db entry")
        addItem = (thanksC.title(), [float(f"{addY:.2f}")])
        donor_db.append(addItem)
elif thanksC.lower() in names:
    nameIndex = names.index(thanksC.lower())
    inList = str(input("That name is in the list, would you like to add a new donation to it? (y/n): "))
    if inList.strip() == "n":
        pass
    if inList.strip() == "y":
        addAmt = float(input("Please enter the new donation amount: "))
        print("Adding " + thanksC.title() + "'s donation of $" + f"{addAmt:.2f}", "to their db entry")
        updateItem = (thanksC.title(), [float(f"{addAmt:.2f}")])
        donor_db.append(updateItem)
        print(nameIndex)
