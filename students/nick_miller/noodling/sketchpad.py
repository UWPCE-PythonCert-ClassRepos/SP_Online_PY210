# #!/usr/bin/env python3
#
# # (or q)
#
# donor_db = [
#             ("William Gates, III", [653772.32, 12.17]),
#             ("Jeff Bezos", [877.33]),
#             ("Paul Allen", [663.23, 43.87, 1.32]),
#             ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
#             ]
# def thank_you():
#     names = []
#     for name, donations in donor_db:
#         name = name.lower()
#         names.append(name)
#     thanks_c = str(input("Enter a name or type 'list': "))
#     thanks_c = thanks_c.lower()
#     if thanks_c.strip() == "q":
#         return
#     if thanks_c.strip() == "list":
#         for i in range(0, (len(donor_db))):
#             entry = (donor_db[i])
#             name = entry[0]
#             print(name)
#     elif thanks_c.lower() not in names:
#         add_q = str(input("That name is not in the list, would you like to add it? (y/n): "))
#         add_q = add_q.lower()
#         if add_q.strip() == "q":
#             return
#         if add_q.strip() == "n":
#             return
#         if add_q.strip() == "y":
#             print("Adding", thanks_c.title(), "to the donor list.")
#             add_y = input("Please enter their donation amount: ")
#             if add_y.lower().strip() == "q":
#                 return
#             else:
#                 add_y = float(add_y)
#                 print("Adding " + thanks_c.title() + "'s donation of $" + f"{add_y:.2f}", "to their db entry")
#                 addItem = (thanks_c.title(), [float(f"{add_y:.2f}")])
#                 donor_db.append(addItem)
#                 firster = thanks_c.title().split()
#                 firster = firster[0]
#                 toters = float(f"{add_y:.2f}")
#                 letter = ('\n'.join(['', 'Dearest {first_name},', '', 'Thank you for your generous support!',
#                                      'We appreciate your donation of ${donats:.2f}.', '',
#                                      'Sincerest regards',
#                                      '',
#                                      'The Foundation'])).format(first_name=firster, donats=toters)
#                 print("Here is your Thank You:")
#                 print(letter)
#     elif thanks_c.lower() in names:
#         name_index = names.index(thanks_c.lower())
#         ind_list = donor_db[name_index]
#         ind_list = list(ind_list)
#         donats = ind_list[1]
#         name_donat = ind_list[0], donats
#         name_donat = tuple(name_donat)
#         in_list = str(input("That name is in the list, would you like to add a new donation to it? (y/n): "))
#         while in_list != "y" and in_list != "n" and in_list != "q":
#             in_list = input("Please enter y or n: ").lower()
#         if in_list == "n":
#             next_q = str(input("Do you still want to send a Thank You? (y/n): "))
#             while next_q != "y" and next_q != "n" and next_q != "q":
#                 next_q = input("Please enter y or n: ").lower()
#             if next_q == "n":
#                 pass
#             if next_q == "q":
#                 return
#             elif next_q == "y":
#                 print("ok, we'll write one now...")
#         elif in_list == "y":
#             ind_list = donor_db[name_index]
#             ind_list = list(ind_list)
#             donats = ind_list[1]
#             add_donats = input("Add a donation amount: ")
#             add_donats = float(add_donats)
#             donats.append(add_donats)
#             name_donat = ind_list[0], donats
#             name_donat = tuple(name_donat)
#         namer = name_donat[0]
#         namer = namer.split()
#         firster = namer[0]
#         monies = name_donat[1]
#         toters = sum(monies)
#
#         letter = ('\n'.join(['', 'Dearest {first_name},', '', 'Thank you for your generous support!',
#                              'We appreciate your donation(s), which total ${donats:.2f} to date!', '', 'Sincerest regards',
#                              '',
#                              'The Foundation'])).format(first_name=firster, donats=toters)
#
#         print("Here is your Thank You:")
#         print(letter)
#
#
# thank_you()


def y_or_n_or_q(ver):
    ver = ver.strip().lower()
    while ver != "y" and ver != "n" and ver != "q":
        ver = input("Please enter y or n: ")
    return ver


y_or_n_or_q(";lkj ")
