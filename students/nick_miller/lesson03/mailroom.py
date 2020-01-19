#!/usr/bin/env python3

# sample data for donor db from tutorial; db is a list of tuples, with a donor name and list of donations

donor_db = [
            ("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]

# The script should prompt the user (you) to choose
# from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

# def


def names_breakout(db=donor_db):
    names = []
    for name, donations in db:
        name = name.lower()
        names.append(name)
    return names


def y_or_n_or_q(ver):
    ver = ver.strip().lower()
    while ver != "y" and ver != "n" and ver != "q":
        ver = input("Please enter y or n: ")
    return ver


# def letter_prep(db=donor_db, ver=thanks_c.lower()):
#     names = names_breakout()
#     name_index = names.index()
#     ind_list = db[name_index]
#     ind_list = list(ind_list)
#     donats = ind_list[1]
#     name_donat = ind_list[0], donats
#     name_donat = tuple(name_donat)
#     return name_donat


def thanks(db=donor_db):
    names = names_breakout()
    thanks_c = str(input("Enter a name or type 'list': "))
    thanks_c = thanks_c.lower()
    if thanks_c.strip() == "list":
        for i in range(0, (len(donor_db))):
            entry = (donor_db[i])
            name = entry[0]
            print(name)
    elif thanks_c.strip().lower() == "q":
        return
    elif thanks_c.lower() not in names:
        add_q = str(input("That name is not in the list, would you like to add it? (y/n): "))
        add_q = add_q.lower()
        if add_q.strip() == "q":
            return
        if add_q.strip() == "n":
            return
        if add_q.strip() == "y":
            print("Adding", thanks_c.title(), "to the donor list.")
            add_y = input("Please enter their donation amount: ")
            if add_y.lower().strip() == "q":
                return
            else:
                add_y = float(add_y)
                print("Adding " + thanks_c.title() + "'s donation of $" + f"{add_y:.2f}", "to their db entry")
                addItem = (thanks_c.title(), [float(f"{add_y:.2f}")])
                donor_db.append(addItem)
                firster = thanks_c.title().split()
                firster = firster[0]
                toters = float(f"{add_y:.2f}")
                letter = ('\n'.join(['', 'Dearest {first_name},', '', 'Thank you for your generous support!',
                                     'We appreciate your donation of ${donats:.2f}.', '',
                                     'Sincerest regards',
                                     '',
                                     'The Foundation'])).format(first_name=firster, donats=toters)
                print("Here is your Thank You:")
                print(letter)
    elif thanks_c.lower() in names:
        name_index = names.index(thanks_c.lower())
        ind_list = donor_db[name_index]
        ind_list = list(ind_list)
        donats = ind_list[1]
        name_donat = ind_list[0], donats
        name_donat = tuple(name_donat)
        in_list = str(input("That name is in the list, would you like to add a new donation to it? (y/n): "))
        while in_list != "y" and in_list != "n" and in_list != "q":
            in_list = input("Please enter y or n: ").lower()
        if in_list == "q":
            return
        if in_list == "n":
            next_q = str(input("Do you still want to send a Thank You? (y/n): "))
            while next_q != "y" and next_q != "n" and next_q != "q":
                next_q = input("Please enter y or n: ").lower()
            if next_q == "n":
                pass
            if next_q == "q":
                return
            elif next_q == "y":
                namer = name_donat[0]
                namer = namer.split()
                firster = namer[0]
                monies = name_donat[1]
                toters = sum(monies)
                letter = ('\n'.join(['', 'Dearest {first_name},', '', 'Thank you for your generous support!',
                                     'We appreciate your donation of ${donats:.2f}.', '',
                                     'Sincerest regards',
                                     '',
                                     'The Foundation'])).format(first_name=firster, donats=toters)
                print(letter)
        elif in_list == "y":
            ind_list = donor_db[name_index]
            ind_list = list(ind_list)
            donats = ind_list[1]
            while True:
                try:
                    add_donats = input("Add a donation amount: ")
                    if add_donats.strip().lower() == "q":
                        return
                    else:
                        add_donats = float(add_donats)
                        donats.append(add_donats)
                        name_donat = ind_list[0], donats
                        name_donat = tuple(name_donat)
                        break
                except ValueError:
                    print("Sorry, that is not a valid amount. ")
        namer = name_donat[0]
        namer = namer.split()
        firster = namer[0]
        monies = name_donat[1]
        toters = sum(monies)

        letter = ('\n'.join(['', 'Dearest {first_name},', '', 'Thank you for your generous support!',
                             'We appreciate your donation(s), which total ${donats:.2f} to date!', '',
                             'Sincerest regards',
                             '',
                             'The Foundation'])).format(first_name=firster, donats=toters)

        print("Here is your Thank You:")
        print(letter)


def report_sort_key(item):
    return item[1]


def report(db=donor_db):
    report_don = []
    for name, donations in db:
        totes = sum(donations)
        nums = len(donations)
        aves = totes / nums
        report_don.append((name, totes, nums, aves))

    report_don.sort(key=report_sort_key, reverse=True)

    key = ["name", "total given", "num gifts", "average gift"]
    separator = "|"

    print(f"{key[0]:<18}",
          f"{separator:^3}",
          f"{key[1]:^18}",
          f"{separator:^3}",
          f"{key[2]:^10}",
          f"{separator:^3}",
          f"{key[3]:>15}")
    print("-" * 76)
    for row in report_don:
        print("{:<18s}   {:>15.2f}   {:12d}   {:>20.2f}".format(*row))


def quit_prog():
    print("Quitting - See you next time.")
    quit()


def main():
    while True:
        print("""
        Menu of Options
        1) Send a 'Thank You'
        2) Create a Report
        3) Exit Program
        """)
        usrchoice = str(input("Which option would you like to perform? [1 to 3]: "))
        print()  # adding a new line

        # Choice 1 -Show the current items in the table
        if usrchoice.strip() == '1':
            thanks()

        elif usrchoice.strip() == '2':
            report()

        elif usrchoice.strip() == '3':
            quit_prog()

        elif usrchoice.strip() == 'q':
            quit_prog()

        else:
            print("sorry, that's not a valid option")


main()
