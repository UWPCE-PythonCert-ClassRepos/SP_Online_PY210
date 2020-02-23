#!/usr/bin/env python3

donor_db = {
    "Jeff Staple": [20, 20],
    "Takashi Murakami": [10.50],
    "Virgil Abloh": [300, 40.33, 5.35],
    "Jan Chipchase": [1001.23, 400.87, 102]
}


def letter_prep(ver, db):
    """
    takes user input (name)
    :param ver: name (sanitized before being passed)
    :param db: a dict of donors and their donations
    :return: a list of their full name, first name, all donations, and a total
    """
    namer = ver.split(" ")
    firster = namer[0]
    monies = db[ver.title()]
    toters = sum(monies)
    toters = float(f"{toters:.2f}")
    return [firster, toters]


def letter_format(firster, toters):
    """
    takes in first name and totals and returns formatted Thank You message
    :param firster: first name, sanitized before passing
    :param toters: sum of donations, sanitized before passing
    :return: formatted, faux-personalized Thank You message
    """
    letter = ('\n'.join(['', 'Dearest {first_name},', '', 'Thank you for your generous support!',
                             'We appreciate your donation(s), which total ${donats:.2f} to date!', '',
                             'Sincerest regards,',
                             '',
                             'The Foundation'])).format(first_name=firster, donats=toters)
    return letter


# def one_thanks(db=donor_db):
#     """
#     this whole thing needs re-tooled to work with the new dict-based db
#     :param db: dictionary-based database of donors(key) and their donations(values)
#     :return: thanks for a donation
#     """
#     thanks_c = str(input("Enter a name or type 'list': "))    # take input here;
#     thanks_c = thanks_c.lower()
#     if thanks_c.strip() == "list":
#         for item in donor_db:
#             print(item)
#     elif thanks_c.strip().lower() == "q":
#         return
#     elif thanks_c.title() not in donor_db.keys():
#         add_q = str(input("That name is not in the list, would you like to add it? (y/n): "))
#         add_q = add_q.lower().strip()
#         if add_q == "q":
#             return
#         elif add_q == "n":
#             return
#         elif add_q == "y":
#             print("Adding", thanks_c.title(), "to the donor list.")
#             add_y = input("Please enter their donation amount: ")
#             if add_y.lower().strip() == "q":
#                 return
#             else:
#                 while True:
#                     try:
#                         add_y = float(add_y)
#                         break
#                     except ValueError:
#                         print("Sorry, that is not a valid amount. ")
#                 add_y_f = f"{add_y:.2f}"
#                 thanks_c = thanks_c.title()
#                 print("Adding " + thanks_c + "'s donation of $" + add_y_f, "to their db entry")
#                 add_y_l = [add_y]
#                 donor_db[thanks_c] = add_y_l
#                 firster = letter_prep(thanks_c, donor_db)[0]
#                 toters = letter_prep(thanks_c, donor_db)[1]
#                 letter = letter_format(firster, toters)
#                 print("Here is your Thank You:")
#                 print(letter)
#     elif thanks_c.title() in donor_db.keys():
#         in_list = str(input("That name is in the list, would you like to add a new donation to it? (y/n): "))
#         while in_list != "y" and in_list != "n" and in_list != "q":
#             in_list = input("Please enter y or n: ").lower()
#         if in_list == "q":
#             return
#         if in_list == "n":
#             next_q = str(input("Do you still want to send a Thank You? (y/n): "))
#             while next_q != "y" and next_q != "n" and next_q != "q":
#                 next_q = input("Please enter y or n: ").lower()
#             if next_q == "n":
#                 pass
#             if next_q == "q":
#                 return
#             elif next_q == "y":
#                 firster = letter_prep(thanks_c, donor_db)[1]
#                 toters = letter_prep(thanks_c, donor_db)[3]
#                 letter = letter_format(firster, toters)
#                 print(letter)
#         elif in_list == "y":
#             donats = donor_db[thanks_c.title()]
#             while True:
#                 try:
#                     add_donats = input("Add a donation amount: ")
#                     if add_donats.strip().lower() == "q":
#                         return
#                     else:
#                         add_donats = float(add_donats)
#                         donats.append(add_donats)
#                         break
#                 except ValueError:
#                     print("Sorry, that is not a valid amount. ")
#         firster = letter_prep(thanks_c, donor_db)[0]
#         toters = letter_prep(thanks_c, donor_db)[1]
#         letter = letter_format(firster, toters)
#         print("Here is your Thank You:")
#         print(letter)

# def thanks_input():
#     thanks_c = str(input("Enter a name or type 'list': "))
#     thanks_c = thanks_c.lower()
#     if thanks_c.strip() == "list":
#         for item in donor_db:
#             print(item)
#     elif thanks_c.strip().lower() == "q":
#         return "exit menu"
#     else:
#         return thanks_c


def ask_user(q):
    answer = input(str(q))
    return answer


def input_prep(thanks_c):
    thanks_c = thanks_c.strip().lower()
    return thanks_c


def list_print(db=None):
    if db is None:
        db = donor_db
    for item in db:
        print(item)


def list_check(thanks_c, db=None):
    if db is None:
        db = donor_db
    if thanks_c.title() in db.keys():
        return thanks_c
    elif thanks_c.title() not in db.keys():
        return "not"


def input_check(thanks_c):
    if thanks_c.strip().lower() == "q":
        return "q"
    elif thanks_c.strip().lower() == "y":
        return "y"
    elif thanks_c.strip().lower() == "y":
        return "n"
    elif thanks_c.strip().lower() == "list":
        return "list"
    else:
        return thanks_c


def don_add(thanks_c, db=None):
    if db is None:
        db = donor_db
    donats = donor_db[thanks_c.title()]
    while True:
        try:
            amount = "Add a donation amount: "
            add_donats = ask_user(amount)
            if add_donats.strip().lower() == "q":
                return
            else:
                add_donats = float(add_donats)
                donats.append(add_donats)
                break
        except ValueError:
            print("Sorry, that is not a valid amount.")


def db_update(new_item_key, new_item_value, db=None):
    if db is None:
        db = donor_db
    db[new_item_key.title()] = [new_item_value]


def one_thanks(db=None):
    if db is None:
        db = donor_db
    q = "please enter a donor name or list: "
    ans = ask_user(q)
    if input_check(ans) == "list":
        list_print(donor_db)
    elif input_prep(ans) in list_check(ans):
        q = "this donor is in the database, would you like to add a donation (y/n): "
        add_or_no = input_check(ask_user(q))
        while add_or_no != "y" and add_or_no != "n" and add_or_no != "q":
            add_or_no = input("Please enter y or n: ").lower()
        if add_or_no == "y":
            don_add(ans, donor_db)
            letter = letter_prep(ans, donor_db)
            letter = letter_format(letter[0], letter[1])
            print(letter)
        elif add_or_no == "n":
            q = "would you still like to create a thank you? (y/n): "
            answ = input_check(ask_user(q))
            while answ != "y" and answ != "n" and answ != "q":
                answ = input("Please enter y or n: ").lower()
            if answ == "y":
                letter = letter_prep(ans, donor_db)
                letter = letter_format(letter[0], letter[1])
                print(letter)
            elif ans == "n":
                return
            elif ans == "q":
                return
        elif add_or_no == "q":
            return
    elif list_check(ans) == "not":
        q = "that name is not in the list, would you like to add it? (y/n): "
        answ = input_check(ask_user(q))
        while answ != "y" and answ != "n" and answ != "q":
            answ = input("Please enter y or n: ").lower()
        if answ == "y":
            q = "please enter a donation amount: "
            amount = float(ask_user(q))
            db_update(ans, amount, donor_db)
            letter = letter_prep(ans, donor_db)
            letter = letter_format(letter[0], letter[1])
            print(letter)
        elif answ == "n":
            return
        elif answ == "q":
            return
    elif input_check(ans) == "q":
        return


one_thanks(donor_db)
