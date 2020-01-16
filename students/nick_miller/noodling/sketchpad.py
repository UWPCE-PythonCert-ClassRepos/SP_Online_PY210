# donor_db = [
#             ("William Gates, III", [653772.32, 12.17]),
#             ("Jeff Bezos", [877.33]),
#             ("Paul Allen", [663.23, 43.87, 1.32]),
#             ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
#             ]
#
#
# def nameslist(db=donor_db):
#     names = []
#     for i in range(0, (len(donor_db))):
#         entry = (donor_db[i])
#         name = entry[0]
#         names.append(name.lower())
#     list(names)
# #
# # # print(names)
# #
# # # def report(db=donor_db):
# # #     print(donor_db)
# # #     print()
# # #     key = ["name", "total given", "num gifts", "average gift"]
# # #     separator = "|"
# # #
# # #     print(f"{key[0]:<18}",
# # #           f"{separator:^3}",
# # #           f"{key[1]:<18}",
# # #           f"{separator:^3}",
# # #           f"{key[2]:>10}",
# # #           f"{separator:^3}",
# # #           f"{key[3]:>15}")
# # #     print("-"*76)
# # #
# # #     for i in range(0, (len(donor_db))):
# # #         entry = (donor_db[i])
# # #         name = entry[0]
# # #         # print(name)
# # #         dons = entry[1]
# # #         totes = sum(dons)
# # #         # print(totes)
# # #         nums = len(dons)
# # #         # print(nums)
# # #         aves = totes/nums
# # #         # print(aves)
# # #         print(f"{name:<18}",
# # #           f"{separator:^3}",
# # #           f"{totes:>18.2f}",
# # #           f"{separator:^3}",
# # #           f"{nums:^10}",
# # #           f"{separator:^3}",
# # #           f"{aves:>15.2f}")
# # #
# # # report()
# #
# # thanksC = str(input("Enter a name or type 'list': "))
# # thanksC = thanksC.lower()
# # if thanksC.strip() == "list":
# #     for i in range(0, (len(donor_db))):
# #         entry = (donor_db[i])
# #         name = entry[0]
# #         print(name)
# # elif thanksC.lower() not in names:
# #     addQ = str(input("That name is not in the list, would you like to add it? (y/n): "))
# #     addQ = addQ.lower()
# #     if addQ.strip() == "n":
# #         pass
# #     if addQ.strip() == "y":
# #         print("Adding", thanksC.title(), "to the donor list.")
# #         addY = float(input("Please enter their donation amount: "))
# #         print("Adding " + thanksC.title() + "'s donation of $" + f"{addY:.2f}", "to their db entry")
# #         addItem = (thanksC.title(), [float(f"{addY:.2f}")])
# #         donor_db.append(addItem)
# # elif thanksC.lower() in names:
# #     nameIndex = names.index(thanksC.lower())
# #     inList = str(input("That name is in the list, would you like to add a new donation to it? (y/n): "))
# #     if inList.strip() == "n":
# #         pass
# #     if inList.strip() == "y":
# #         addAmt = float(input("Please enter the new donation amount: "))
# #         print("Adding " + thanksC.title() + "'s donation of $" + f"{addAmt:.2f}", "to their db entry")
# #         updateItem = (thanksC.title(), [float(f"{addAmt:.2f}")])
# #         donor_db.append(updateItem)
# #         print(nameIndex)
#
# # words = ['maritus', 'et', 'quolibet', 'is', 'habitancium', 'dico', 'locum~locus', 'domus', 'totus', 'tempus', 'vitis', 'is', 'de', 'quolibet', 'ipse']
# #
# # words2 = words
# #
# # words2 = str(words2)
# #
# # print(words2)
# #
# # print(words2.find("cram"))
# #
# # print(words)
#
#
# # def thanks(db=donor_db):
# #     thanksC = str(input("Enter a name or type 'list': "))
# #     thanksC = thanksC.lower()
# #     if thanksC.strip() == 'list':
# #         for i in range(0, (len(donor_db))):
# #             entry = (donor_db[i])
# #             name = entry[0]
# #             print(name)
# #     elif thanksC in names:
# #         finditem = names.index(thanksC)
# #         donor_db_new = list(donor_db)
# #         listtoaddto = donor_db_new[finditem]
# #         addY = addY = str(input("Please enter their donation amount: "))
# #         addY = float(f"{addY:.2f}")
# #         listtoaddto = listtoaddto[1]
# #         listtoaddto.append(addY)
# #         donor_db_new = tuple(donor_db_new)
# #     elif thanksC not in donor_db:
# #         addQ = str(input("That name is not in the list, would you like to add it? (y/n)"))
# #         if addQ.strip() == "n":
# #             pass
# #         if addQ.strip() == "y":
# #             print("Adding ", thanksC.capitalize(), " to the donor list.")
# #             addY = str(input("Please enter their donation amount: "))
#
# def thanks(db=donor_db):
#     thanksC = str(input("Enter a name or type 'list': "))
#     thanksC = thanksC.lower()
#     if thanksC.strip() == 'list':
#         for i in range(0, (len(donor_db))):
#             entry = (donor_db[i])
#             name = entry[0]
#             print(name)
#     elif thanksC not in nameslist():
#         addQ = str(input("That name is not in the list, would you like to add it? (y/n)"))
#         if addQ.strip() == "n":
#             pass
#         if addQ.strip() == "y":
#             print("Adding ", thanksC.capitalize(), " to the donor list.")
#             addY = str(input("Please enter their donation amount: "))
#
#
# thanks()

fruits = ["Oranges", "Peaches", "Apples", "Pineapples"]


# def yesorno(question):
#     reply = str(input(question + ' (y/n): ')).lower().strip()
#     if reply[0] == 'y':
#         return True
#     if reply[0] == 'n':
#         return False
#     else:
#         return yesorno("Please respond with a 'y' or an 'n'. " + question + ":")
# delfruits = []
#
# for fruit in fruits:
#     question = "Do you like " + fruit + "? (y/n): "
#     yesorno = input(question)
#     drop = fruits.index(fruit)
#     while yesorno != "y" and yesorno != "n":
#         yesorno = input("Please enter y or n: ").lower()
#     if yesorno == "n":
#         delfruits.append(drop)
# for i in delfruits:
#     fruits.pop(i)
#
# print(fruits)

backwardsfruits = []
for i in fruits:
    i = i[::-1]
    backwardsfruits.append(i)

print(backwardsfruits)

del fruits[-1]
print(fruits)
